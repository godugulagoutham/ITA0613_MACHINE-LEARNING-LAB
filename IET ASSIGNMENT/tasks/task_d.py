"""TASK D: Adapted Candidate-Elimination / version-space analysis."""
from pathlib import Path
import numpy as np
import pandas as pd
from src.candidate_elimination import CandidateElimination
def run_task_d(df,train,results_dir):
    tables=Path(results_dir)/'tables'; dcols=['Annual_Rainfall','Temperature','Humidity']
    for c in dcols:
        q1,q2=train[c].quantile([.33,.66]); df[c+'_band']=pd.cut(df[c],[-np.inf,q1,q2,np.inf],labels=['Low','Medium','High'])
    q1,q2=train.Yield.quantile([.33,.66]); df['Yield_band']=pd.cut(df.Yield,[-np.inf,q1,q2,np.inf],labels=['Low','Medium','High'])
    data=df.loc[train.index,[c+'_band' for c in dcols]+['Yield_band']].dropna(); ce=CandidateElimination([['Low','Medium','High']]*3,'High'); history=[]
    for i,row in data.head(250).iterrows():
        S,G=ce.update(tuple(row[c+'_band'] for c in dcols),str(row.Yield_band)); history.append({'row_index':int(i),'label':str(row.Yield_band),'S':str(S),'G_size':len(G)})
    out=pd.DataFrame(history); out.to_csv(tables/'task_d_candidate_elimination_history.csv',index=False); return out
