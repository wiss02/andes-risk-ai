# Contributing to ANDES-RISK AI

Thanks for your interest. ANDES-RISK AI is an **independent, early-stage research initiative**. Contributions should make analysis more reproducible, safer, and more scientifically sound.

## Suggested contributions

- Improve Python tests and documentation.
- Review CSV validation, temporal leakage guards and statistical metrics.
- Propose ethically sourced geospatial datasets, with verified citations and licenses.
- Review experimental design, sample bias and reporting of uncertainty.

## Getting started

```bash
git clone https://github.com/wiss02/andes-risk-ai.git
cd andes-risk-ai
python -m pip install -e .
python -m unittest discover -s tests -v
python -m andes_risk generate-demo
python -m andes_risk evaluate --input data/synthetic_demo.csv
```

Open an issue describing the change and scientific rationale. For substantial changes, propose a research protocol before implementation. Use pull requests with tests, documentation, source citations and explicit limitations.

## Integrity and safety

- Never invent datasets, labels, performance numbers, publications, institutional collaborators or lab affiliations.
- Clearly label synthetic, simulated, preliminary and observed results.
- Do not upload personal or restricted data.
- Do not use outputs to advise evacuations or life-safety decisions.
- Data and AI tools must be used under their own terms and licenses.

## Academic affiliation

ANDES-RISK AI is not currently an official research group of UNED, SIMDA or another university. Contribution does not imply such affiliation.
