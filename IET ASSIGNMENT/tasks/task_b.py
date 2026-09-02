"""TASK B: First-principles kNN regression."""
from pathlib import Path
import pandas as pd
from src.knn_regressor import KNNRegressorScratch
from src.metrics import regression_metrics
def run_task_b(X_train,y_train,X_val,y_val,X_test,y_test,results_dir):
    tables=Path(results_dir)/'tables'; rows=[]
    for metric in ['euclidean','mahalanobis']:
        for k in [1,3,5,7,9,11,15,21]:
            p=KNNRegressorScratch(k,metric).fit(X_train,y_train).predict(X_val); rows.append({'metric':metric,'k':k,**regression_metrics(y_val,p)})
    val=pd.DataFrame(rows); best=val.sort_values('RMSE').iloc[0]; model=KNNRegressorScratch(int(best.k),best.metric).fit(X_train,y_train); pred=model.predict(X_test); metrics=regression_metrics(y_test,pred)
    val.to_csv(tables/'task_b_knn_validation.csv',index=False); pd.DataFrame([{'metric':best.metric,'k':int(best.k),**metrics}]).to_csv(tables/'task_b_knn_test_results.csv',index=False); pd.DataFrame({'y_true':y_test,'y_pred_knn':pred}).to_csv(tables/'task_b_knn_predictions.csv',index=False)
    return {'validation':val,'best':best,'pred':pred,'metrics':metrics}
