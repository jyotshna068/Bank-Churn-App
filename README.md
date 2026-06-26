# 🏦 Bank Customer Churn Prediction using CatBoost & Streamlit

## 📌 Overview

This project is an end-to-end Machine Learning application that predicts whether a bank customer is likely to churn (leave the bank) based on customer demographics, account information, and banking behavior.

The model is trained using **CatBoost Classifier** with advanced feature engineering and is deployed as an interactive **Streamlit** web application. The application not only predicts churn probability but also categorizes customer risk, recommends retention strategies, and provides explainable AI insights using **SHAP (SHapley Additive Explanations)**.

---

## 🚀 Features

* Predict customer churn probability in real time
* Customer risk categorization

  * 🟢 Low Risk
  * 🟡 Moderate Risk
  * 🟠 Medium Risk
  * 🔴 High Risk
* Personalized retention recommendations
* Explainable AI using SHAP
* Interactive Streamlit dashboard
* Feature importance visualization
* User-friendly interface for customer analysis

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* CatBoost
* Scikit-learn
* SHAP
* Matplotlib
* Streamlit

---

## 📂 Dataset

Dataset: **Churn Modelling Dataset**

Features include:

* Credit Score
* Geography
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Credit Card Ownership
* Active Membership
* Estimated Salary

Target Variable:

* **Exited**

  * 0 → Customer Stayed
  * 1 → Customer Churned

---

## ⚙️ Feature Engineering

The following engineered features were created to improve model performance:

* BalanceSalaryRatio
* TenureByAge
* CreditScoreAgeRatio
* BalancePerProduct
* ProductsPerAge
* IsSenior

These engineered features capture relationships between customer demographics and banking behavior, improving predictive capability.

---

## 🤖 Machine Learning Model

Algorithm Used:

* CatBoost Classifier

Model Configuration:

* Iterations: 2000
* Depth: 8
* Learning Rate: 0.03
* Evaluation Metric: ROC-AUC
* Auto Class Weights: Balanced
* Early Stopping Enabled

---

## 📊 Model Performance

| Metric        | Score     |
| ------------- | --------- |
| Accuracy      | **85%** |
| ROC-AUC Score | **86.9%** |

Additional Evaluation:

* Classification Report
* Confusion Matrix
* Feature Importance Analysis
* SHAP Explainability

---

## 📈 Explainable AI

The project integrates **SHAP (SHapley Additive Explanations)** to explain individual predictions.

The dashboard provides:

* Feature contribution analysis
* SHAP value interpretation
* Natural language explanation of the top contributing features

This improves model transparency and helps understand why a customer is predicted to churn.

---

## 💻 Streamlit Application

The web application allows users to:

* Enter customer details
* Predict churn probability
* View customer risk level
* Receive retention recommendations
* Analyze feature contributions using SHAP
* Review customer input summary

---

## 📁 Project Structure

```
Bank-Churn-App/
│
├── app.py
├── bank_churn_model.cbm
├── requirements.txt
├── README.md
└── churn_prediction.ipynb
```
