#EXPERIMENT NO 11 CREDIT SCORE CLASSIFICATION
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# Sample credit data (you can replace with CSV later)
data = {
    "Income": [30, 50, 70, 20, 90, 60, 40, 80],
    "Age": [22, 35, 45, 25, 50, 40, 30, 48],
    "Loan": [5, 10, 8, 3, 12, 6, 4, 9],
    "Approved": [0, 1, 1, 0, 1, 1, 0, 1]  # 1 = Good credit, 0 = Bad credit
}

df = pd.DataFrame(data)
X = df[["Income", "Age", "Loan"]]
y = df["Approved"]

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42)

model = LogisticRegression()
model.fit(Xtr, ytr)
yp = model.predict(Xte)

print("Accuracy:", accuracy_score(yte, yp))

cm = confusion_matrix(yte, yp)
ConfusionMatrixDisplay(cm).plot()
plt.title("Confusion Matrix - Credit Score Classification")
plt.show()
