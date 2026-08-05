# EXPERIMENT NO 16 Compare different types Classification Algorithms and evaluate their performance.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import matplotlib.pyplot as plt

X,y = load_iris(return_X_y=True)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

models = {
    "LR":LogisticRegression(max_iter=200),
    "KNN":KNeighborsClassifier(),
    "DT":DecisionTreeClassifier(),
    "NB":GaussianNB(),
    "SVM":SVC()
}

acc=[]
for name,model in models.items():
    model.fit(X_train,y_train)
    acc.append(model.score(X_test,y_test))

plt.bar(models.keys(),acc)
plt.ylabel("Accuracy")
plt.show()
