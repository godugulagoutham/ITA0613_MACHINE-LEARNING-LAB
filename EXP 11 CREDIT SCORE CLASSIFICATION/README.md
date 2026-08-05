# Credit Score Classification

## 📌 Overview

This project implements a **Credit Score Classification** system using Machine Learning. The objective is to classify customers into different credit score categories (Good, Standard, or Poor) based on their financial and personal information. The model is trained using historical customer data and predicts the credit score of new customers accurately.

---

## 🎯 Objective

- To develop a machine learning model for credit score classification.
- To preprocess and analyze customer financial data.
- To train and evaluate a classification model.
- To predict the credit score category of customers.

---

## 📂 Dataset

The dataset contains customer financial information such as:

- Age
- Occupation
- Annual Income
- Monthly Salary
- Number of Bank Accounts
- Number of Credit Cards
- Interest Rate
- Number of Loans
- Delay from Due Date
- Outstanding Debt
- Credit Utilization Ratio
- Monthly Balance
- Payment Behaviour
- Credit Score (Target)

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📚 Machine Learning Algorithm

This project uses a **Random Forest Classifier** (or any suitable classification algorithm) to classify customer credit scores based on the available features.

---

## ⚙️ Steps Performed

1. Import the required libraries.
2. Load the dataset.
3. Explore and analyze the dataset.
4. Handle missing values.
5. Encode categorical features.
6. Split the dataset into training and testing sets.
7. Train the classification model.
8. Predict the credit score for test data.
9. Evaluate the model using various performance metrics.
10. Display the prediction results.

---

## 📊 Evaluation Metrics

The model performance is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

---

## 📁 Project Structure

```
Credit-Score-Classification/
│
├── credit_score.csv
├── credit_score_classification.py
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

Install the required Python libraries using:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## ▶️ Run the Project

Execute the following command:

```bash
python credit_score_classification.py
```

---

## 📈 Output

The program displays:

- Dataset information
- Data preprocessing results
- Model training status
- Predicted Credit Score
- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 💡 Applications

- Banking Sector
- Loan Approval Systems
- Credit Card Eligibility
- Financial Risk Assessment
- Insurance Companies
- FinTech Applications

---

## 🚀 Future Enhancements

- Hyperparameter tuning for improved accuracy.
- Deploy the model as a web application using Flask or Streamlit.
- Integrate real-time customer data.
- Compare multiple machine learning algorithms.

---

## ✅ Conclusion

The Credit Score Classification model successfully predicts customer credit score categories using machine learning techniques. This system assists financial institutions in making faster and more accurate credit decisions while reducing manual effort and financial risk.
