# EXPERIMENT NO 19 Naive Bayes classification for Bank Loan prediction
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample dataset
data = pd.DataFrame({
    'Income':[50000,60000,30000,80000,25000,70000],
    'Credit_Score':[700,650,600,750,580,720],
    'Loan_Status':['Yes','Yes','No','Yes','No','Yes']
})

# Encoding
le = LabelEncoder()
data['Loan_Status'] = le.fit_transform(data['Loan_Status'])

X = data[['Income','Credit_Score']]
y = data['Loan_Status']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1)

model = GaussianNB()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

print("Accuracy:",accuracy_score(y_test,y_pred))

cm = confusion_matrix(y_test,y_pred)
sns.heatmap(cm,annot=True,fmt='d')
plt.title("Confusion Matrix")
plt.show()

# Class probabilities
probs = model.predict_proba(X_test)
print("Class Probabilities:\n",probs)
