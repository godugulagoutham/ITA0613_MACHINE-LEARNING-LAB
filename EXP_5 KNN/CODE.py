#EXPERIMENT NO (5) KNN

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

X, y = load_iris(return_X_y=True)

accuracy = []
k_values = range(1, 11)

for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X, y)
    accuracy.append(model.score(X, y))

plt.plot(k_values, accuracy, marker='o')
plt.xlabel("K Value")
plt.ylabel("Accuracy")
plt.title("KNN Accuracy vs K")
plt.show()
