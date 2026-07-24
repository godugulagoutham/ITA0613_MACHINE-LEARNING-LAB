# Experiment 2: Candidate Elimination Algorithm

## 📌 Objective
To implement and demonstrate the **Candidate Elimination Algorithm** using Python to find the set of all hypotheses that are consistent with the given training examples.

---

## 📖 Description

The Candidate Elimination Algorithm is a supervised machine learning algorithm used for concept learning. It identifies all hypotheses that are consistent with the training data by maintaining two boundaries:

- **Specific Boundary (S):** The most specific hypothesis.
- **General Boundary (G):** The most general hypothesis.

As each training example is processed, these boundaries are updated to represent the version space containing all consistent hypotheses.

---

## 🎯 Aim

To implement the Candidate Elimination Algorithm in Python using a CSV dataset and determine the Specific Boundary (S) and General Boundary (G) of the hypothesis space.

---

## 🛠️ Software Requirements

- Python 3.x
- Jupyter Notebook / Google Colab / Visual Studio Code
- Pandas Library
- NumPy Library

---

## 📚 Theory

The Candidate Elimination Algorithm is based on the concept of **Version Space**, which consists of all hypotheses that correctly classify the given training examples.

The algorithm maintains two sets of hypotheses:

- **Specific Boundary (S):** Represents the most specific consistent hypothesis.
- **General Boundary (G):** Represents the most general consistent hypothesis.

For every training example:
- If the example is positive, the Specific Boundary is generalized.
- If the example is negative, the General Boundary is specialized.

The algorithm continues updating both boundaries until all training examples have been processed.

---

## 📝 Algorithm

1. Read the training dataset from a CSV file.
2. Initialize the Specific Boundary (S) with the first positive training example.
3. Initialize the General Boundary (G) with the most general hypothesis.
4. For each training example:
   - If the example is **positive**, generalize the Specific Boundary and remove inconsistent hypotheses from the General Boundary.
   - If the example is **negative**, specialize the General Boundary and remove inconsistent hypotheses.
5. Repeat until all training examples are processed.
6. Display the final Specific Boundary (S) and General Boundary (G).

---

## 🔄 Procedure

1. Install Python and the required libraries.
2. Import the necessary Python modules.
3. Load the dataset from a CSV file.
4. Initialize the Specific and General boundaries.
5. Process each training example.
6. Update the boundaries based on the class label.
7. Remove inconsistent hypotheses.
8. Display the final Version Space consisting of S and G.

---

## 📂 Input

A CSV file containing:

- Training Attributes
- Target Class (Yes/No)

Example Attributes:
- Sky
- Air Temperature
- Humidity
- Wind
- Water
- Forecast
- Enjoy Sport (Target)

---


## 💡 Applications

- Concept Learning
- Knowledge Discovery
- Pattern Recognition
- Medical Diagnosis
- Data Classification
- Artificial Intelligence

---

## ✅ Advantages

- Finds all hypotheses consistent with the training data.
- Uses both positive and negative examples.
- Represents the complete Version Space.
- Useful for concept learning problems.

---

## ❌ Limitations

- Computationally expensive for large datasets.
- Sensitive to noisy or inconsistent data.
- Requires a finite hypothesis space.
- Difficult to implement for complex problems.

---
## 🏁 Conclusion

The Candidate Elimination Algorithm was successfully implemented using Python. The algorithm generated the Specific Boundary (S) and General Boundary (G), representing all hypotheses consistent with the given training examples. This experiment demonstrates concept learning using Version Space in machine learning.

---

## 📈 output
<img width="1283" height="747" alt="Image" src="https://github.com/user-attachments/assets/68004278-1f3c-45fc-9355-f5ade40dff7a" />

---



## 👨‍💻 Author

**Name:** GODUGULA GOUTHAM (192312187)
**Course:** B.E. Electronics and Communication Engineering  
**Subject:** Machine Learning Laboratory  
**Experiment:** Candidate Elimination Algorithm
