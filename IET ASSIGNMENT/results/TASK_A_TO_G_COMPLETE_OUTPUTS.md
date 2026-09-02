# Task A–G Output Index

The local validated package produced 8 PNG visualisations and task/result CSV tables. This GitHub version contains the complete source pipeline, technical report, policy brief, tests and CI, plus the validated summary below.

## Validated run
- 20,000 benchmark records
- Train: 16,743
- Validation: 1,583
- Test: 1,674
- kNN: Mahalanobis, k=21, RMSE 1.8182
- LWR: tau=2.0, RMSE 1.8201
- A→G pipeline: successful
- pytest: passed

## Required final-data action
Replace the benchmark CSV with a qualifying public dataset (≥10,000 records, multi-year and multi-region) before academic submission, then rerun the pipeline so all result tables/figures correspond to the real source data.
