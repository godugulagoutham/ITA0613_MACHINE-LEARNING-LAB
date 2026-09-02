"""TASK G: Evaluation, uncertainty and fairness audit."""
from pathlib import Path
import numpy as np
import pandas as pd
def run_task_g(test,y_test,knn_pred,lwr_pred,results_dir):
    tables=Path(results_dir)/'tables'; audit=test[['State','Crop','Crop_Year']].copy(); audit['abs_error_knn']=np.abs(y_test-knn_pred); audit['abs_error_lwr']=np.abs(y_test-lwr_pred); state=audit.groupby('State')[['abs_error_knn','abs_error_lwr']].mean().reset_index(); crop=audit.groupby('Crop')[['abs_error_knn','abs_error_lwr']].mean().reset_index(); state.to_csv(tables/'task_g_state_error_audit.csv',index=False); crop.to_csv(tables/'task_g_crop_error_audit.csv',index=False); return state,crop
