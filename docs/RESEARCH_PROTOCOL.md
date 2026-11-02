# Protocolo de investigación | Research protocol

> **Status: proposal, not validated scientific findings.** ANDES-RISK AI is an independent, student-led research initiative. This document is a pre-experiment plan. The first Python baseline only evaluates **synthetic data**.

## Research question

Under carefully controlled spatial and temporal validation, can transparent machine-learning baselines and AI-assisted reproducible data workflows improve the **quality of analysis** of rainfall-associated landslide events in Andean settings compared with simple reference methods?

We distinguish **research on modelling** from an operational **hazard-warning service**. Success on synthetic data is evidence about software correctness, not evidence of real-world predictive skill.

## Proposed hypotheses

- **H1 (model skill):** On a properly sourced observational dataset, a multivariable rainfall-and-topography model may outperform a constant-prevalence baseline on pre-specified proper scoring rules (Brier score), after temporal and spatial evaluation. This hypothesis is **untested**.
- **H2 (workflow quality):** A documented preprocessing and audit workflow may reduce non-reproducible data transformations relative to ad hoc manual preprocessing. This hypothesis is **untested**.
- **H3 (agent contribution, later stage):** Subject to comparable budgets and blinded review, an AI-assisted data-quality audit may identify a higher proportion of seeded data errors than an unaided baseline while maintaining an acceptable false-positive rate. This hypothesis is **untested**.

## Experimental phases

### Phase A — Software-methodology pilot (current)

1. Generate deterministic synthetic observations, clearly labelled as invented.
2. Validate schema and basic invariants.
3. Fit a transparent logistic regression on the training portion.
4. Perform a chronological train/test holdout; derive scalers only from training data.
5. Report confusion matrix, accuracy, precision, recall, F1, false-alarm rate and Brier score versus a prevalence-only baseline.
6. Record configuration, versions, random seed and execution instructions.

**What this phase cannot show:** Bolivian hazard frequency, actual spatial risk, satellite predictive accuracy, or suitability for public safety decisions.

### Phase B — Observational data feasibility (planned)

1. Identify a source for **verified event labels** and a clearly documented location/time unit of analysis.
2. Review temporal/spatial coverage, missingness, observational biases, measurement uncertainty and data licensing.
3. Evaluate spatial/temporal joins between precipitation, terrain and events; explicitly test data leakage and duplicated events.
4. Draft an ethics, safety and expert-review protocol before training real-world models.
5. Publish data provenance and code. If source terms disallow redistribution, publish a documented acquisition procedure instead.

### Phase C — Scientific evaluation (planned)

- Time-forward evaluation and **geographically held-out** locations.
- Compare baseline prevalence, rainfall-only and rainfall-plus-terrain approaches.
- Compare Brier score, calibration, precision/recall and false alarm/missed-event tradeoffs.
- Report per-region and per-period sample sizes, and confidence intervals where justified.
- Document uncertainty and distribution shifts; do not use absolute probabilities without validation.

### Phase D — Multi-agent research assistance (planned)

Explore agents for metadata extraction, data-quality checking, reproducible code generation and report drafting. A separate independent evaluator should verify their outputs. Agents must not fabricate field observations, override provenance checks or automatically issue public warnings.

## Data leakage controls

- Fit feature transforms and imputers **inside** each training fold only.
- Do not random-split correlated events across neighboring regions and dates without explicit justification.
- Audit label construction and exclude information unavailable at the intended prediction time.
- Separate model selection from final held-out evaluation.
- Track seeds, checksums and training-data versions.

## Interpretive safeguards

- Report how event inventories are incomplete and potentially biased toward reported events.
- Avoid implying that missing events are evidence of absence.
- Keep synthetic scoring separate from observational results.
- Before any operational use, require domain-expert review, validated local observations, calibration, monitoring and acceptance by responsible public authorities.

## Proposed outputs

Documented reproducibility scripts; open-source prototype; source and data dictionary; experiment log; transparently reported failures; scientific technical report. No publications, impact metrics, awards or lab affiliations are claimed to have been achieved.
