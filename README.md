# ANDES-RISK AI

**Investigación abierta sobre IA y análisis experimental de deslizamientos en Bolivia.**  
**Open research on AI and experimental landslide analysis in Bolivia.**

[![Python tests](https://github.com/wiss02/andes-risk-ai/actions/workflows/tests.yml/badge.svg)](https://github.com/wiss02/andes-risk-ai/actions/workflows/tests.yml)
[![Live demo](https://img.shields.io/badge/Live_demo-Render-84e5b3)](https://andes-risk-ai.onrender.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Stage: prototype](https://img.shields.io/badge/Stage-Experimental-orange)](docs/RESEARCH_PROTOCOL.md)

**[🌐 Ver demostración web](https://andes-risk-ai.onrender.com/)** · **[🔬 Protocolo científico](docs/RESEARCH_PROTOCOL.md)** · **[🛰 Fuentes de datos](docs/DATA_SOURCES.md)** · **[🏗 Arquitectura](docs/ARCHITECTURE.md)** · **[🤝 Contribuir](CONTRIBUTING.md)**

> **Aviso científico:** la versión actual emplea únicamente datos sintéticos; no es un sistema de predicción real, de gestión de emergencias ni de alertas para Bolivia. Es una iniciativa independiente, sin afiliación oficial a UNED o SIMDA.

## ¿Qué problema investigamos?

¿Cómo podemos evaluar de manera reproducible métodos computacionales para estudiar la relación entre precipitaciones, relieve y registros de deslizamientos, y qué aportan los agentes de IA como asistentes de investigación?

## Estado de desarrollo

| Disponible actualmente | Investigación futura |
| --- | --- |
| Generador reproducible de datos sintéticos | Integración de datos satelitales con procedencia |
| Validación CSV y regresión logística de referencia | Comparación con datos de eventos verificados |
| División temporal entrenamiento/prueba | Validación espacial, calibración e incertidumbre |
| Métricas y pruebas de software | Agentes auditores y análisis geoespacial |
| Página interactiva estática y mapa base geográfico en Render | Capas y mapas científicos contrastados por expertos |

**Los objetivos futuros no son funciones terminadas.**

## Reproducir el prototipo (Python 3.10+)

```bash
git clone https://github.com/wiss02/andes-risk-ai.git
cd andes-risk-ai
python -m pip install -e .
python -m andes_risk generate-demo --output data/synthetic_demo.csv --seed 42
python -m andes_risk evaluate --input data/synthetic_demo.csv --output results/metrics.json
python -m unittest discover -s tests -v
```

**Documento de investigación:** [hipótesis, metodología, sesgos y controles de calidad](docs/RESEARCH_PROTOCOL.md).  
**Procedencia de datos:** [fuentes candidatas y criterios de aceptación](docs/DATA_SOURCES.md).  
**Arquitectura:** [flujo disponible y propuesta futura diferenciados](docs/ARCHITECTURE.md).

---

## Research question

Can reproducible computational workflows and, in later phases, specialized AI agents improve the evaluation of rainfall-associated landslide susceptibility in Andean settings?

The initial version is a **software-methodology demonstrator using entirely synthetic observations**. Its probabilities, scores, dates and site IDs do **not** reflect real Bolivian hazard. No claim of forecasting accuracy is made. **Do not use for emergency planning, evacuation, site selection, or public warnings.**

## Current capabilities (v0.1)

- Generate reproducible **synthetic** precipitation, slope, and event data using a fixed random seed.
- Validate CSV columns and physically plausible input ranges.
- Fit an interpretable regularized logistic-regression baseline using Python's standard library.
- Evaluate with a chronological train/test split and training-only feature normalization.
- Report confusion-matrix counts, accuracy, precision, recall, F1, false-alarm rate, and Brier score against a constant baseline.
- Run unit tests in GitHub Actions.

The web interface includes a geographic reference basemap; it does not contain hazard layers. There is **no satellite download, real event catalog, validated landslide prediction, or AI-agent orchestration yet**. These are research milestones, not delivered capabilities.

## Quick start / Inicio rápido

Requires **Python 3.10+**. No runtime third-party dependencies.

```bash
python -m pip install -e .
python -m andes_risk generate-demo --output data/synthetic_demo.csv --rows 240 --seed 42
python -m andes_risk evaluate --input data/synthetic_demo.csv --output results/metrics.json --data-kind synthetic
python -m unittest discover -s tests -v
```

The generated CSV and JSON metrics are ignored by Git to discourage accidental publication of misunderstood demo results. Run from a local clone. Outputs are explicitly labelled as experimental and non-operational.

### Input CSV schema

`date,site_id,rainfall_24h_mm,rainfall_7d_mm,slope_deg,landslide_observed`

- `date`: ISO 8601 YYYY-MM-DD; `site_id`: nonempty location identifier.
- `rainfall_24h_mm`, `rainfall_7d_mm`: nonnegative rain totals; the 7-day total must be at least the 24-hour total.
- `slope_deg`: 0–90; `landslide_observed`: independently established binary label 0 or 1.
- Using **real** data requires documented source, license, spatial/temporal alignment, missing-data treatment, and expert validation. Merely setting `--data-kind observational` does not establish provenance.

## Scientific roadmap / Hoja de ruta

1. **Data provenance:** assess NASA GPM IMERG rainfall, NASA Global Landslide Catalog, digital elevation models and appropriately licensed local records, recording coverage and limitations. The NASA catalog is not a complete local ground-truth inventory.
2. **Research design:** define spatial/temporal resolution and labels, check for reporting bias, leakage and class imbalance; design out-of-region and time-forward evaluation.
3. **Model comparison:** compare transparent baselines against carefully justified ML alternatives, report uncertainty and calibration.
4. **Agent experiments:** evaluate whether AI-assisted ingestion, data-quality review, code tests and reproducibility audits outperform non-agent workflows.
5. **Responsible reporting:** publish openly licensed code and a technical report, with uncertainties and review by qualified geoscience/domain researchers.

**Primary public scientific references (not integrated yet):**
- NASA GPM IMERG: https://gpm.nasa.gov/data/imerg
- NASA Global Landslide Catalog: https://data.nasa.gov/dataset/global-landslide-catalog-export
- NASA LHASA research: https://github.com/nasa/lhasa

## Academic and safety disclosure / Declaración

ANDES-RISK AI es una **iniciativa científica independiente en fase inicial**. No pertenece oficialmente a la UNED ni a SIMDA. Este prototipo utiliza exclusivamente **datos sintéticos**, y sus resultados no representan predicciones reales de deslizamientos, mapas de amenaza ni alertas para Bolivia.

A future proposal for Google Antigravity must disclose the actual research affiliation accurately; a public GitHub repository does not replace verification of an institution-affiliated laboratory.

## License

MIT — see [LICENSE](LICENSE). External datasets remain subject to their own terms and attribution requirements.

