# ITA0613 Technical Report — Interlinked A→G Pipeline

## Objective
Complete climate-resilient crop-yield pipeline covering data engineering, first-principles kNN/LWR, Candidate-Elimination, scalability, visualisation, policy interpretation, uncertainty/fairness, and reproducibility.

## Data
The current repository uses a 20,000-row synthetic-but-realistic benchmark only because no qualifying public dataset was supplied with the assignment. The final academic run must replace it with a real public agro-climatic dataset and document its official source/licence.

## A — Data Engineering
Numeric weather/soil values are coerced and imputed by state median then global median. Derived features are GDD, rainfall anomaly, temperature range and heat stress. Chronological split: training through 2016, validation 2017–2018, test 2019 onward.

## B — kNN
Euclidean and Mahalanobis distances are implemented from scratch. Candidate k values are 1, 3, 5, 7, 9, 11, 15 and 21. Validation selects the lowest-RMSE pair, then the model is evaluated on the held-out test period.

## C — LWR
Gaussian weighting uses `w_i(x)=exp(-||x-x_i||²/(2 tau²))`. A local weighted linear model is fitted for each query. Small k/tau gives lower bias and higher variance; larger values give higher bias and lower variance.

## D — Version Space
Rainfall, temperature, humidity and yield are discretised into Low/Medium/High. Candidate-Elimination updates S and G. Its inductive bias is the restricted conjunctive hypothesis language.

## E — Scalability
Brute-force timing and memory are measured at 10³, 10⁴, 10⁵ and 10⁶ records. A from-scratch exact k-d tree is benchmarked on 10,000 five-dimensional points.

## F — Visualisation and Policy
Eight Matplotlib figures are produced. Forecasts are positioned as decision support; higher-error regions/crops require stronger monitoring and models should be recalibrated when climate conditions shift.

## G — Limitations, uncertainty and fairness
Historical models can fail under distribution shift, extreme events and unrepresentative observations. Error is audited by state and crop. Forecasts should include uncertainty and subgroup diagnostics.

## SDGs
The intended application supports climate-aware food production decisions linked to SDG 2 (Zero Hunger) and climate adaptation linked to SDG 13 (Climate Action).

## Reproducibility
`pip install -r requirements.txt`, then `python main.py` and `pytest -q`. Generated figures/tables/logs are written to `results/`.
