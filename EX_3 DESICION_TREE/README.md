# 🌳 Experiment 3: Decision Tree using ID3 Algorithm

## 📌 Objective

To implement and demonstrate the **Decision Tree (ID3) Algorithm** using Python, construct a decision tree from a given dataset, and classify a new sample based on the generated model.

---

## 📖 Description

The **ID3 (Iterative Dichotomiser 3)** algorithm is a supervised machine learning algorithm used for classification tasks. It builds a decision tree by selecting the attribute with the highest **Information Gain** at each node. The resulting tree is used to predict the class label of new data instances.

---

## 🎯 Aim

To implement the Decision Tree (ID3) Algorithm using Python, build a decision tree from the given dataset, and classify new samples accurately.

---

## 🛠️ Software Required

- Python 3.x
- Jupyter Notebook / Google Colab / Visual Studio Code
- Pandas
- NumPy
- Scikit-learn
- Matplotlib (Optional)
- Graphviz (Optional, for tree visualization)

---

## 📚 Theory

A Decision Tree is a supervised learning algorithm used for both classification and regression. The ID3 algorithm constructs the tree using a top-down greedy approach. At each step, it selects the attribute with the highest Information Gain, which best separates the training examples into different classes.

The process continues recursively until all training samples belong to the same class or no further attributes remain.

---

## 📝 Algorithm

1. Read the dataset.
2. Calculate the entropy of the dataset.
3. Compute the Information Gain for each attribute.
4. Select the attribute with the highest Information Gain as the root node.
5. Split the dataset based on the selected attribute.
6. Repeat the process recursively for each subset.
7. Stop when all records belong to the same class or no attributes remain.
8. Use the generated decision tree to classify new samples.

---

## 🔄 Procedure

1. Install Python and the required libraries.
2. Import the necessary Python packages.
3. Load the dataset from a CSV file.
4. Preprocess the dataset by separating features and target labels.
5. Encode categorical values if necessary.
6. Split the dataset into training and testing sets.
7. Train the Decision Tree model using the ID3 algorithm.
8. Generate and visualize the decision tree.
9. Test the model using the test dataset or a new sample.
10. Display the predicted class and evaluate the model accuracy.

---

## 📂 Input

A CSV dataset containing:

- Feature Attributes
- Target Class

Example:

- Outlook
- Temperature
- Humidity
- Wind
- Play Tennis (Target)

---



## 💡 Applications

- Medical Diagnosis
- Customer Segmentation
- Credit Risk Analysis
- Weather Prediction
- Spam Email Detection
- Fraud Detection

---

## ✅ Advantages

- Easy to understand and interpret.
- Handles both categorical and numerical data.
- Requires minimal data preprocessing.
- Can visualize decision-making clearly.

---

## ❌ Limitations

- Can overfit if the tree becomes very deep.
- Sensitive to noisy datasets.
- Small changes in data may produce different trees.
- May become complex for large datasets.

---

## 📈 OUTPUT 

<img width="1817" height="586" alt="Image" src="https://github.com/user-attachments/assets/fc0e5827-b3eb-40b4-82fb-9b2e3ee4bb60" />

---

## 🏁 Conclusion

The Decision Tree using the ID3 algorithm was successfully implemented in Python. The model constructed the decision tree based on Information Gain and correctly classified new samples, demonstrating the effectiveness of decision tree learning for classification problems.

---

## 👨‍💻 Author

**Name:** GODUGULA GOUTHAM(192312187)
**Course:** B.E. Electronics and Communication Engineering  
**Subject:** Machine Learning Laboratory  
**Experiment:** Decision Tree using ID3 Algorithm
