# EXPERIMENT NO 17 Implement Mobile Price Prediction using appropriate machine learning algorithm



import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([[2],[4],[6],[8],[12]])  # RAM
y = np.array([8000,12000,16000,20000,30000])

model = LinearRegression()
model.fit(X,y)

print("Predicted price for 10GB:",model.predict([[10]]))

plt.scatter(X,y)
plt.plot(X,model.predict(X))
plt.show()
