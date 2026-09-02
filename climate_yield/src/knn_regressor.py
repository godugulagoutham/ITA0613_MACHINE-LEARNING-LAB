import numpy as np

def euclidean_distance(a,b): return float(np.sqrt(np.sum((np.asarray(a,float)-np.asarray(b,float))**2)))
def mahalanobis_inverse_covariance(X): return np.linalg.pinv(np.cov(np.asarray(X,float),rowvar=False)+1e-8*np.eye(np.asarray(X).shape[1]))
def mahalanobis_distance(a,b,inv_cov):
    d=np.asarray(a,float)-np.asarray(b,float); return float(np.sqrt(max(d.T@inv_cov@d,0.0)))

class KNNRegressorScratch:
    def __init__(self,k=5,metric="euclidean"): self.k=int(k); self.metric=metric
    def fit(self,X,y):
        self.X=np.asarray(X,float); self.y=np.asarray(y,float)
        if self.k<1 or self.k>len(self.X): raise ValueError("invalid k")
        self.inv_cov=mahalanobis_inverse_covariance(self.X) if self.metric=="mahalanobis" else None
        return self
    def predict(self,Q):
        Q=np.asarray(Q,float); out=[]
        for q in Q:
            if self.metric=="euclidean": d=np.sqrt(np.sum((self.X-q)**2,axis=1))
            elif self.metric=="mahalanobis":
                z=self.X-q; d=np.sqrt(np.maximum(np.einsum("ij,jk,ik->i",z,self.inv_cov,z),0))
            else: raise ValueError("unknown metric")
            idx=np.argpartition(d,self.k-1)[:self.k]; out.append(self.y[idx].mean())
        return np.asarray(out)
