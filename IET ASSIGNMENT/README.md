# ITA0613 — Climate-Resilient Crop Yield Forecasting

Complete interlinked Task A–G implementation using NumPy/Pandas/Matplotlib and first-principles ML implementations. The pipeline runs A → B → C → D → E → F → G through `main.py`.

## Important dataset note
The included `data/raw/benchmark_crop_climate.csv` is a reproducible benchmark generated for pipeline validation. It is **not** the required public dataset for final submission. Replace it with a qualifying public multi-year, multi-region agro-climatic dataset (≥10,000 records), then rerun `python main.py`.

## Tasks
- **A:** EDA, cleaning, weather/soil imputation, feature engineering.
- **B:** kNN regression from scratch with Euclidean and Mahalanobis distances and validation-based k selection.
- **C:** Gaussian-kernel Locally Weighted Regression from scratch with bandwidth tuning and bias/variance discussion.
- **D:** Adapted Candidate-Elimination / version-space analysis on discretized yield-risk classes.
- **E:** 10³–10⁶ scalability benchmark and k-d tree prototype.
- **F:** Publication-quality visualizations and agricultural policy brief.
- **G:** Error/uncertainty/fairness audit, climate-change limitations, SDG 2 and SDG 13 linkage.

## Run
```bash
pip install -r requirements.txt
python main.py
pytest -q
```

Outputs are written to `results/` and task-specific tables are also produced there. Core models do not use scikit-learn.

## Final validation run
20,000 benchmark rows; train 16,743; validation 1,583; test 1,674. Best kNN metric: Mahalanobis, k=21, test RMSE ≈ 1.8182. Best LWR bandwidth: tau=2.0, test RMSE ≈ 1.8201. The pipeline completed A → G successfully and the test suite passed.
