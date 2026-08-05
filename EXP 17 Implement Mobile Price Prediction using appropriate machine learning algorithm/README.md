# Mobile Price Prediction using Machine Learning

## 📌 Overview

This project implements a **Mobile Price Prediction** model using Machine Learning. The objective is to predict the price range of a mobile phone based on its technical specifications. The model analyzes various smartphone features and classifies the mobile device into the appropriate price category.

---

## 🎯 Objective

- To build a machine learning model for mobile price prediction.
- To preprocess and analyze the mobile dataset.
- To train and evaluate a classification model.
- To predict the price range of a mobile phone based on its specifications.

---

## 📂 Dataset

The dataset contains various smartphone specifications, including:

- Battery Power
- Bluetooth
- Clock Speed
- Dual SIM
- Front Camera
- Internal Memory
- Mobile Depth
- Mobile Weight
- Number of Cores
- Primary Camera
- Pixel Height
- Pixel Width
- RAM
- Screen Height
- Screen Width
- Talk Time
- 3G Support
- 4G Support
- Wi-Fi Support
- Price Range (Target)

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

The project uses a **Random Forest Classifier** to classify mobile phones into different price ranges based on their specifications. Other classification algorithms such as Decision Tree, K-Nearest Neighbors (KNN), or Support Vector Machine (SVM) can also be used.

---

## ⚙️ Steps Performed

1. Import the required libraries.
2. Load the mobile price dataset.
3. Explore and preprocess the dataset.
4. Handle missing values and encode categorical data if necessary.
5. Split the dataset into training and testing sets.
6. Train the Random Forest classification model.
7. Predict the mobile price range.
8. Evaluate the model using classification metrics.
9. Display the prediction results.

---

## 📊 Evaluation Metrics

The model performance is evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report
---

## ▶️ Installation

Install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## ▶️ Run the Project

Execute the following command:

```bash
python mobile_price_prediction.py
```

---

## 📈 Output

---

## 💡 Applications

- Smartphone Manufacturing
- Mobile Retail Stores
- E-commerce Platforms
- Product Recommendation Systems
- Market Price Analysis
- Consumer Decision Support

---

## 🚀 Future Enhancements

- Improve prediction accuracy using advanced machine learning algorithms.
- Perform hyperparameter tuning.
- Develop a web application using Flask or Streamlit.
- Integrate real-time mobile market data.

---

## ✅ Conclusion

The Mobile Price Prediction model successfully classifies smartphones into different price ranges based on their specifications. It demonstrates the effectiveness of machine learning in predicting product price categories and supports better decision-making for manufacturers, retailers, and consumers.
