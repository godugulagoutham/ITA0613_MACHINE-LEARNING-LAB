#EXPERIMENT NO 13 CAR PRICE PREDICTION

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# Sample dataset (Engine size vs Price)
X = np.array([[1000],[1200],[1500],[1800],[2000]])
y = np.array([200000,250000,300000,350000,400000])
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
# Evaluation
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
print("MSE:", mse)
print("RMSE:", rmse)
# Plot
plt.scatter(X, y, label="Actual")
plt.plot(X, y_pred, color='red', label="Predicted")
plt.legend()
plt.show()
