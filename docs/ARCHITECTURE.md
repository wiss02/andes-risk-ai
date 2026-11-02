# Architecture / Arquitectura

## Current executable path (v0.1)

```mermaid
flowchart TD
  A[Seeded synthetic observation generator] --> B[CSV schema and range validation]
  B --> C[Chronological holdout split]
  C --> D[Training-only normalization + logistic regression]
  D --> E[Held-out evaluation]
  E --> F[Confusion matrix, Brier and baseline metrics]
  F --> G[Local JSON report]
```

- **Python package:** `src/andes_risk/`.
- **Entry point:** `python -m andes_risk` or `andes-risk` after editable install.
- **Tests:** `tests/`, run with `python -m unittest discover -s tests -v`.
- **Static site:** `public/`, deployed on Render. Its synthetic slider visualization is independent of the Python model. It is **not** a production inference frontend.
- **Infrastructure:** `render.yaml` publishes the static `public` directory.

## Research target architecture (NOT IMPLEMENTED)

```mermaid
flowchart LR
  NASA[Licensed public environmental datasets] --> ING[Provenance and ingestion]
  EVENT[Verified event labels] --> ING
  ING --> QA[Quality, joins, metadata and leakage audits]
  QA --> BASE[Simple reference models]
  QA --> ML[Experimental statistical / ML models]
  BASE --> EVAL[Temporal + spatial evaluation]
  ML --> EVAL
  EVAL --> REPORT[Reproducible research reports]
  AGENT[Optional research-support agents] -.Audits only.-> QA
  AGENT -.Assists only.-> REPORT
```

Do not interpret the target diagram as functionality already delivered.

## Design principles

1. Keep scientific data provenance explicit and auditable.
2. Preserve deterministic, low-dependency baselines.
3. Make synthetic and observational experiments distinguishable in results and reports.
4. Respect temporal/spatial holdouts and guard against leakage.
5. Keep AI-generated code and scientific claims subject to independent validation.
6. Never issue automatic risk warnings from unvalidated models.

## Extending the project

Future packages could include `ingestion/`, `geospatial/`, `models/`, `agents/` and `reporting/`. These are *proposed modules*, not part of v0.1.
