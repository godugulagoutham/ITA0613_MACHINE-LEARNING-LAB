import numpy as np
def regression_metrics(y,p):
    y,p=np.asarray(y,float),np.asarray(p,float); mse=np.mean((y-p)**2); denom=np.sum((y-y.mean())**2)
    return {"MAE":float(np.mean(np.abs(y-p))),"MSE":float(mse),"RMSE":float(np.sqrt(mse)),"R2":float(1-np.sum((y-p)**2)/denom) if denom else 0.0}
