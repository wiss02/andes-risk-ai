"""Reproducible baseline for *experimental* landslide-event classification.

This is a demonstrator, not a validated hazard or emergency-warning model.
Synthetic events and parameters do not describe observed conditions in Bolivia.
"""
from __future__ import annotations

import csv
import math
import random
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

FEATURES = ("rainfall_24h_mm", "rainfall_7d_mm", "slope_deg")
COLUMNS = ("date", "site_id", *FEATURES, "landslide_observed")


@dataclass(frozen=True)
class Observation:
    day: date
    site_id: str
    rainfall_24h_mm: float
    rainfall_7d_mm: float
    slope_deg: float
    event: int

    @property
    def features(self) -> tuple[float, float, float]:
        return self.rainfall_24h_mm, self.rainfall_7d_mm, self.slope_deg


@dataclass(frozen=True)
class LogisticModel:
    mean: tuple[float, float, float]
    scale: tuple[float, float, float]
    weights: tuple[float, float, float]
    intercept: float

    def probability(self, features: tuple[float, float, float]) -> float:
        standardized = [(v - mu) / s for v, mu, s in zip(features, self.mean, self.scale)]
        z = self.intercept + sum(w * x for w, x in zip(self.weights, standardized))
        z = min(35.0, max(-35.0, z))
        return 1.0 / (1.0 + math.exp(-z))


def make_synthetic_csv(path: str | Path, n: int = 240, seed: int = 42) -> Path:
    """Generate clearly labeled fake data for testing the software pipeline."""
    if n < 40:
        raise ValueError("Use at least 40 synthetic observations.")
    rng = random.Random(seed)
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(COLUMNS)
        for i in range(n):
            r24 = round(rng.gammavariate(2.0, 16.0), 2)
            r7 = round(r24 + rng.gammavariate(3.0, 25.0), 2)
            slope = round(10 + rng.random() * 45, 2)
            latent = -5.0 + 0.035 * r24 + 0.012 * r7 + 0.04 * slope
            probability = 1.0 / (1.0 + math.exp(-latent))
            event = int(rng.random() < probability)
            writer.writerow([
                (date(2025, 1, 1) + timedelta(days=i)).isoformat(),
                "SYNTHETIC_SITE",
                r24, r7, slope, event,
            ])
    return destination


def load_observations(path: str | Path) -> list[Observation]:
    observations: list[Observation] = []
    with Path(path).open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames or not set(COLUMNS).issubset(reader.fieldnames):
            raise ValueError("CSV columns required: " + ", ".join(COLUMNS))
        for number, row in enumerate(reader, start=2):
            try:
                day = date.fromisoformat(row["date"])
                site = row["site_id"].strip()
                vals = tuple(float(row[key]) for key in FEATURES)
                label = int(row["landslide_observed"])
                if not site or label not in (0, 1):
                    raise ValueError("Invalid site or binary label")
                if not all(math.isfinite(v) for v in vals):
                    raise ValueError("Non-finite measurements")
                if vals[0] < 0 or vals[1] < vals[0] or not (0 <= vals[2] <= 90):
                    raise ValueError("Invalid rainfall or slope values")
                observations.append(Observation(day, site, *vals, label))
            except (ValueError, TypeError, KeyError, AttributeError) as exc:
                raise ValueError(f"Invalid CSV row {number}: {exc}") from exc
    if len(observations) < 40:
        raise ValueError("At least 40 observations are required.")
    return observations


def fit_logistic(train: list[Observation], epochs: int = 600, rate: float = 0.12) -> LogisticModel:
    """Simple regularized logistic regression, implemented with Python's stdlib."""
    n = len(train)
    mean = tuple(sum(row.features[j] for row in train) / n for j in range(3))
    scale = tuple(max(1.0, (sum((row.features[j] - mean[j]) ** 2 for row in train) / n) ** 0.5)
                  for j in range(3))
    x = [tuple((row.features[j] - mean[j]) / scale[j] for j in range(3)) for row in train]
    y = [row.event for row in train]
    weights = [0.0, 0.0, 0.0]
    intercept = 0.0
    for _ in range(epochs):
        gradients = [0.0, 0.0, 0.0]
        bias_gradient = 0.0
        for features, label in zip(x, y):
            z = min(35.0, max(-35.0, intercept + sum(w * v for w, v in zip(weights, features))))
            error = 1.0 / (1.0 + math.exp(-z)) - label
            bias_gradient += error
            for j in range(3):
                gradients[j] += error * features[j]
        intercept -= rate * bias_gradient / n
        for j in range(3):
            weights[j] -= rate * (gradients[j] / n + 0.01 * weights[j])
    return LogisticModel(mean, scale, tuple(weights), intercept)


def _safe_ratio(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def evaluate(observations: list[Observation], train_fraction: float = 0.75) -> dict:
    """Chronological holdout; training-derived normalization avoids temporal leakage."""
    if not 0.5 <= train_fraction <= 0.9:
        raise ValueError("train_fraction must be between 0.5 and 0.9")
    if len(observations) < 40:
        raise ValueError("At least 40 observations are required")
    ordered = sorted(observations, key=lambda r: (r.day, r.site_id))
    cut = int(len(ordered) * train_fraction)
    train, test = ordered[:cut], ordered[cut:]
    if train[-1].day >= test[0].day:
        raise ValueError("Train/test share a date; choose observations with a clean temporal boundary")
    model = fit_logistic(train)
    probabilities = [model.probability(r.features) for r in test]
    predicted = [int(p >= 0.5) for p in probabilities]
    tp = sum(p == 1 and r.event == 1 for p, r in zip(predicted, test))
    tn = sum(p == 0 and r.event == 0 for p, r in zip(predicted, test))
    fp = sum(p == 1 and r.event == 0 for p, r in zip(predicted, test))
    fn = sum(p == 0 and r.event == 1 for p, r in zip(predicted, test))
    precision = _safe_ratio(tp, tp + fp)
    recall = _safe_ratio(tp, tp + fn)
    baseline_rate = sum(r.event for r in train) / len(train)
    result = {
        "research_only": True,
        "warning": "NOT an operational landslide prediction or emergency warning system",
        "features": list(FEATURES),
        "train_count": len(train),
        "test_count": len(test),
        "train_end_date": train[-1].day.isoformat(),
        "test_start_date": test[0].day.isoformat(),
        "threshold": 0.5,
        "confusion_matrix": {"tp": tp, "tn": tn, "fp": fp, "fn": fn},
        "metrics": {
            "accuracy": _safe_ratio(tp + tn, len(test)),
            "precision": precision,
            "recall": recall,
            "f1": _safe_ratio(2 * precision * recall, precision + recall),
            "false_alarm_rate": _safe_ratio(fp, fp + tn),
            "brier_score": sum((p - r.event) ** 2 for p, r in zip(probabilities, test)) / len(test),
            "constant_baseline_brier_score":
                sum((baseline_rate - r.event) ** 2 for r in test) / len(test),
        },
    }
    return result
