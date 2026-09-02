# ITA0613 — Interlinked Climate-Resilient Crop Yield Forecasting Pipeline

![CI](https://github.com/godugulagoutham/ITA0613-climate-yield/actions/workflows/tests.yml/badge.svg)

This repository is an end-to-end A→G implementation of the ITA0613 Machine Learning assignment. It covers NumPy/Pandas data engineering, first-principles kNN and LWR, adapted Candidate-Elimination/version-space analysis, scalability testing with an indexing prototype, Matplotlib visualisations, policy interpretation, tests and CI.

## Important dataset note
The included `data/raw/benchmark_crop_climate.csv` is a **20,000-row synthetic-but-realistic reproducibility benchmark** because the assignment file did not include the required public agro-climatic dataset. Replace it with a qualifying public dataset (≥10,000 rows, multi-year, multi-region) before final submission and update the schema mapping if necessary.

## Pipeline

`main.py` runs A → B → C → D → E → F → G in sequence, passing outputs between stages.

- **A:** cleaning, state-median imputation, derived climate features, chronological split, standardisation.
- **B:** Euclidean + Mahalanobis kNN, manual validation curve and best-k selection.
- **C:** Gaussian-kernel locally weighted regression with manual bandwidth validation.
- **D:** Low/Medium/High yield-risk discretisation and adapted Candidate-Elimination boundaries.
- **E:** 10³→10⁶ scalability benchmark and exact k-d tree prototype.
- **F:** eight Matplotlib figures and a policy brief.
- **G:** state/crop error audits, limitations and fairness evidence.

## Run

```bash
python -m pip install -r requirements.txt
python main.py
pytest -q
```

Outputs are written to `results/`.

## Academic submission
The assignment requires genuine incremental GitHub history. The development history for this folder should be maintained as staged commits: scaffold → data engineering → kNN → LWR → version space → scalability → visualisation/policy → tests/CI → final results/report.
