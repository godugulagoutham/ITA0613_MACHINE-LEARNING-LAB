"""TASK F: Publication-quality visualisations and policy brief."""
from pathlib import Path
from src.visualization import make_plots
def run_task_f(df,knn_val,lwr_val,scalability,model_metrics,results_dir):
    make_plots(df,knn_val,lwr_val,scalability,model_metrics,Path(results_dir)/'plots')
    brief='''# Policy Brief — Climate-Resilient Crop Yield Forecasting\n\nThe integrated pipeline uses climate and soil history to support crop-yield planning. Forecasts should be used as decision support rather than automatic planting instructions. Regions and crops with higher errors should receive stronger local monitoring.\n\nThe analysis supports **SDG 2 (Zero Hunger)** through improved climate-aware planning and **SDG 13 (Climate Action)** through adaptation to climate variability.\n\nModel validation and subgroup diagnostics should be repeated whenever new climate regimes or crops are introduced.\n'''
    Path(results_dir,'task_f_policy_brief.md').write_text(brief,encoding='utf-8')
