#EXPERIMENT NO 10  EXPECTION AND MAXIMIZATION ALGORITHM
import numpy as np, matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

X, _ = make_blobs(n_samples=300, centers=3, random_state=42)

gmm = GaussianMixture(n_components=3, random_state=42)
gmm.fit(X)
labels = gmm.predict(X)

print("Means:\n", gmm.means_)
print("Covariances:\n", gmm.covariances_)

plt.scatter(X[:,0], X[:,1], c=labels)
plt.title("EM Clustering using GMM")
plt.show()
