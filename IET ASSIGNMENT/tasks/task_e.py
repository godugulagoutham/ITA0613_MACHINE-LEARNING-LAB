"""TASK E: Scalability and k-d tree optimisation prototype."""
from pathlib import Path
import time
import numpy as np
import pandas as pd
from src.scalability import brute_force_knn_time
from src.kdtree import KDTreeScratch
def run_task_e(results_dir):
    tables=Path(results_dir)/'tables'; rng=np.random.default_rng(42); rows=[]
    for n in [10**3,10**4,10**5,10**6]:
        X=rng.normal(size=(n,5)); q=rng.normal(size=5); rows.append({'N':n,'seconds':brute_force_knn_time(X,q),'memory_MB':X.nbytes/(1024**2)})
    scale=pd.DataFrame(rows); scale.to_csv(tables/'task_e_scalability.csv',index=False); X=rng.normal(size=(10000,5)); q=rng.normal(size=5); t=time.perf_counter(); tree=KDTreeScratch(X); build=time.perf_counter()-t; t=time.perf_counter(); ki,_=tree.query(q); kd=time.perf_counter()-t; t=time.perf_counter(); bi=int(np.argmin(np.sum((X-q)**2,axis=1))); brute=time.perf_counter()-t; kdout=pd.DataFrame([{'N':10000,'build_seconds':build,'kd_query_seconds':kd,'brute_query_seconds':brute,'same_nearest':ki==bi}]); kdout.to_csv(tables/'task_e_kdtree_summary.csv',index=False); return scale,kdout
