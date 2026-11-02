"""Command-line interface for reproducible baseline experiments."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .core import evaluate, load_observations, make_synthetic_csv


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="ANDES-RISK AI: experimental research, NOT operational hazard alerts"
    )
    sub = parser.add_subparsers(dest="command", required=True)
    demo = sub.add_parser("generate-demo", help="Generate SYNTHETIC input data")
    demo.add_argument("--output", type=Path, default=Path("data/synthetic_demo.csv"))
    demo.add_argument("--rows", type=int, default=240)
    demo.add_argument("--seed", type=int, default=42)

    run = sub.add_parser("evaluate", help="Chronological logistic-regression evaluation")
    run.add_argument("--input", type=Path, required=True)
    run.add_argument("--output", type=Path, default=Path("results/metrics.json"))
    run.add_argument("--data-kind", choices=("synthetic", "observational"), default="synthetic",
                     help="Provenance label for results; use observational only for verified real records")

    args = parser.parse_args(argv)
    if args.command == "generate-demo":
        result = make_synthetic_csv(args.output, n=args.rows, seed=args.seed)
        print(f"Generated synthetic-only dataset: {result}")
    elif args.command == "evaluate":
        observations = load_observations(args.input)
        metrics = evaluate(observations)
        metrics["data_kind_declared"] = args.data_kind
        metrics["source_file"] = str(args.input)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(metrics, indent=2, sort_keys=True) + "\n",
                               encoding="utf-8")
        print(json.dumps(metrics, indent=2, sort_keys=True))
        print(f"Saved experimental metrics to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
