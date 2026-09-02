# ITA0613 — Task-by-Task Code and Outputs




## Task A — Data Engineering & EDA

Clean data, impute missing climate/soil values, engineer GDD, rainfall anomaly, temperature range and heat stress, then summarize and visualize.

**Code:** `task_a/task_a.py`

**Console output:** `task_a/output.txt`

**Generated outputs:** all PNG/CSV files inside `task_a/`.

### What to write in your final report

Explain the cleaning decisions, missing-value imputation method, merged-data logic if using multiple public files, and the meaning of each engineered feature. Include the two EDA figures.

## Task B — kNN Regression

Implement Euclidean and Mahalanobis distances from scratch, manually select k from a validation curve, and evaluate MAE/MSE/RMSE/R².

**Code:** `task_b/task_b.py`

**Console output:** `task_b/output.txt`

**Generated outputs:** all PNG/CSV files inside `task_b/`.

### What to write in your final report

Show the Euclidean and Mahalanobis equations, explain the kNN algorithm, show the validation curve, state the selected k, and compare MAE/RMSE/R².

## Task C — Locally Weighted Regression

Implement Gaussian-kernel LWR from scratch, tune bandwidth tau and explain the bias-variance trade-off relative to kNN.

**Code:** `task_c/task_c.py`

**Console output:** `task_c/output.txt`

**Generated outputs:** all PNG/CSV files inside `task_c/`.

### What to write in your final report

Derive the Gaussian weight, explain W and the weighted normal equation, report the selected bandwidth, and discuss low/high locality as bias-variance trade-offs.

## Task D — Candidate-Elimination

Discretize yield and climate variables, maintain S and G version-space boundaries, and explain inductive bias.

**Code:** `task_d/task_d.py`

**Console output:** `task_d/output.txt`

**Generated outputs:** all PNG/CSV files inside `task_d/`.

### What to write in your final report

Show the discretisation scheme, initial S/G, representative boundary updates, final boundaries, and explain the hypothesis-space inductive bias.

## Task E — Scalability & Optimisation

Benchmark brute-force search from 10³ to 10⁶ records and prototype a k-d tree.

**Code:** `task_e/task_e.py`

**Console output:** `task_e/output.txt`

**Generated outputs:** all PNG/CSV files inside `task_e/`.

### What to write in your final report

Give O(nd) distance cost and memory reasoning, show measured scaling, and compare brute-force search with the k-d tree prototype.

## Task F — Visualisations & Policy Brief

Generate at least five publication-quality plots and turn the observed climate-yield patterns into policy recommendations.

**Code:** `task_f/task_f.py`

**Console output:** `task_f/output.txt`

**Generated outputs:** all PNG/CSV files inside `task_f/`.

### What to write in your final report

Insert all six figures, then provide a short non-technical policy brief with climate-risk actions and SDG 2/13 linkage.

## Task G — Limitations, Uncertainty, Fairness & SDGs

Audit uncertainty/error, fairness across groups, limitations under climate change, and connect the solution to SDG 2 and SDG 13.

**Code:** `task_g/task_g.py`

**Console output:** `task_g/output.txt`

**Generated outputs:** all PNG/CSV files inside `task_g/`.

### What to write in your final report

Discuss historical-data limitations, uncertainty, fairness by geography/crop/season, and why predictions should be used as decision support rather than exact guarantees.

## Final checklist
- Replace benchmark data with a qualifying real public dataset.
- Rerun tasks A–G.
- Copy regenerated outputs into `results/`.
- Run `pytest -q`.
- Commit incrementally to GitHub.
- Add README, report and GitHub Actions CI as required by the assignment.
