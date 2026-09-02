"""TASK C: First-principles Locally Weighted Regression."""
from pathlib import Path
import pandas as pd
from src.locally_weighted_regression import LWRRegressorScratch
from src.metrics import regression_metrics
def run_task_c(X_train,y_train,X_val,y_val,X_test,y_test,results_dir):
    tables=Path(results_dir)/'tables'; rows=[]
    for tau in [.2,.5,.8,1.0,1.5,2.0]:
        p=LWRRegressorScratch(tau,max_neighbors=200).fit(X_train,y_train).predict(X_val); rows.append({'tau':tau,**regression_metrics(y_val,p)})
    val=pd.DataFrame(rows); best_tau=float(val.sort_values('RMSE').iloc[0].tau); pred=LWRRegressorScratch(best_tau,max_neighbors=200).fit(X_train,y_train).predict(X_test); metrics=regression_metrics(y_test,pred)
    val.to_csv(tables/'task_c_lwr_validation.csv',index=False); pd.DataFrame([{'tau':best_tau,'max_neighbors':200,**metrics}]).to_csv(tables/'task_c_lwr_test_results.csv',index=False); pd.DataFrame({'y_true':y_test,'y_pred_lwr':pred}).to_csv(tables/'task_c_lwr_predictions.csv',index=False)
    return {'validation':val,'best_tau':best_tau,'pred':pred,'metrics':metrics}
