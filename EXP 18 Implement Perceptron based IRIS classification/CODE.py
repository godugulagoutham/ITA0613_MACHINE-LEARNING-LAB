# EXPERIMENT NO 18 Implement Perceptron based IRIS classification

from sklearn.datasets import load_iris
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X,y = load_iris(return_X_y=True)
X = X[:,:2]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

model = Perceptron(max_iter=1000)
model.fit(X_train,y_train)

print("Accuracy:",accuracy_score(y_test,model.predict(X_test)))
