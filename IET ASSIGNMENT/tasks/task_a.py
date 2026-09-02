"""TASK A: Data Engineering & EDA."""
from pathlib import Path
import pandas as pd
from src.data_preprocessing import clean_and_engineer,time_split,MODEL_FEATURES,standardize
def run_task_a(raw_path,results_dir):
    tables=Path(results_dir)/'tables'; tables.mkdir(parents=True,exist_ok=True); raw=pd.read_csv(raw_path); df=clean_and_engineer(raw); df.to_csv(tables/'task_a_cleaned_engineered_data.csv',index=False)
    train,val,test=time_split(df); Xtr,[Xv,Xte],mu,sd=standardize(train,[val,test],MODEL_FEATURES)
    return {'data':df,'train':train,'validation':val,'test':test,'X_train':Xtr,'X_val':Xv,'X_test':Xte,'y_train':train.Yield.to_numpy(),'y_val':val.Yield.to_numpy(),'y_test':test.Yield.to_numpy()}
