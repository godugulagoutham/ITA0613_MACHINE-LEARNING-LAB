import numpy as np

def gaussian_kernel(distance_squared,tau):
    if tau<=0: raise ValueError("tau must be positive")
    return np.exp(-distance_squared/(2.0*tau*tau))

class LWRRegressorScratch:
    def __init__(self,tau=1.0,max_neighbors=200): self.tau=float(tau); self.max_neighbors=int(max_neighbors)
    def fit(self,X,y):
        self.X=np.asarray(X,float); self.y=np.asarray(y,float); self.X1=np.c_[np.ones(len(self.X)),self.X]; return self
    def predict(self,Q):
        Q=np.asarray(Q,float); out=[]
        for q in Q:
            d2=np.sum((self.X-q)**2,axis=1); m=min(self.max_neighbors,len(self.X)); idx=np.argpartition(d2,m-1)[:m]
            Xl=self.X1[idx]; yl=self.y[idx]; w=gaussian_kernel(d2[idx],self.tau)+1e-10
            theta=np.linalg.pinv(Xl.T@(w[:,None]*Xl))@(Xl.T@(w*yl)); out.append(np.r_[1.0,q]@theta)
        return np.asarray(out)
