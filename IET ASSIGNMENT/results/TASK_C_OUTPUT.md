# Task C — Locally Weighted Regression Output

Best validation bandwidth: tau=2.0.

Test metrics:
- MAE: 1.3546
- RMSE: 1.8201
- R²: -0.0212

LWR uses a bounded 200-neighbour local fit for computational feasibility.

## Output files
- `tables/lwr_validation.csv`
- `tables/lwr_test_results.csv`
- `tables/lwr_predictions.csv`
- `plots/06_lwr_validation_curve.png`
