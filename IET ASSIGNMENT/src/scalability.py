import time
import numpy as np
def brute_force_knn_time(X,q,k=5):
    t0=time.perf_counter(); d2=np.sum((X-q)**2,axis=1); np.argpartition(d2,k-1)[:k]; return time.perf_counter()-t0
