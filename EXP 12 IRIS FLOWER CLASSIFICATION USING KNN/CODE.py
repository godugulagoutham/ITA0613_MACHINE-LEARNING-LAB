#EXPERIMENT NO 12 IRIS FLOWER CLASSIFICATION USING KNN

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)

ks, accs = range(1, 11), []
for k in ks:
    m = KNeighborsClassifier(n_neighbors=k).fit(Xtr, ytr)
    accs.append(accuracy_score(yte, m.predict(Xte)))
    print(f"K={k}, Accuracy={accs[-1]:.3f}")

plt.plot(list(ks), accs, marker='o')
plt.xlabel("K"); plt.ylabel("Accuracy"); plt.title("Accuracy vs K (Iris + KNN)")
plt.show()
