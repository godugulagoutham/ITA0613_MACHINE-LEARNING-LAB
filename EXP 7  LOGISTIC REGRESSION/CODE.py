#EXPERIMENT NO 7  LOGISTIC REGRESSION
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

# Simple dataset
X = np.array([[1],[2],[3],[4],[5],[6]])
y = np.array([0,0,0,1,1,1])

# Train model
model = LogisticRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

print("Confusion Matrix:\n", confusion_matrix(y, y_pred))
print("Accuracy:", accuracy_score(y, y_pred))

# Sigmoid graph
x = np.linspace(-10, 10, 100)
sig = 1 / (1 + np.exp(-x))

plt.plot(x, sig)
plt.title("Sigmoid Function")
plt.show()
