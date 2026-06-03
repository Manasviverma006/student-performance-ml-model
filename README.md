# student-performance-ml-model
ml model to predict student performance using decision tree algorithm
# Student Performance Prediction ML Model 📊🎓

An end-to-end Machine Learning project that utilizes the **Decision Tree Algorithm** to predict student academic performance based on various demographic, social, and academic factors. 

---

## 🚀 Project Overview
Predicting student performance helps educational institutions identify students who might need extra support early in the academic cycle. This project explores data preprocessing, feature selection, and the implementation of a Decision Tree Classifier to classify or predict student outcomes.

## 🛠️ Tech Stack & Libraries
* **Language:** Python 🐍
* **Libraries:** 
  * `pandas` & `numpy` (Data Manipulation & Preprocessing)
  * `scikit-learn` (Model Building, Training, and Evaluation)
  * `matplotlib` & `seaborn` (Data Visualization)

---

## 📈 Methodology

1. **Data Preprocessing & EDA:**
   * Handled missing values and checked for data imbalances.
   * Encoded categorical variables (e.g., school, gender, address) into numerical values using Label Encoding / One-Hot Encoding.
   * Explored feature correlations to understand what impacts student grades the most.

2. **Model Training:**
   * Split the dataset into training and testing sets ($80\%$ train, $20\%$ test).
   * Built a `DecisionTreeClassifier` using `scikit-learn`.
   * *[Optional: Mention if you limited hyper-parameters, e.g., "Tuned `max_depth` to prevent overfitting."]*

3. **Evaluation:**
   * Evaluated the model using Accuracy, Precision, Recall, and a Confusion Matrix.

---

## 📊 Key Results & Insights
* **Model Accuracy:** `XX%` *(Replace with your model's actual test accuracy, e.g., 82%)*
* **Top Features Driving Success:** 
  1. Past academic performance (e.g., previous semester grades)
  2. Weekly study time
  3. School attendance rate

> 💡 **Fun Fact:** The Decision Tree allowed us to visually trace the exact "if-else" logic the model used to determine whether a student would pass or excel!

---

## 💻 How to Run This Project Locally

1. **Clone the repository:**
```bash
   git clone [https://github.com/Manasviverma006/student-performance-ml-model.git](https://github.com/Manasviverma006/student-performance-ml-model.git)
   cd student-performance-ml-model
