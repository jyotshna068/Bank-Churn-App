# 🏦 Bank Customer Churn Prediction

An end-to-end Machine Learning Web Application that predicts whether a bank customer is likely to churn using a CatBoost Classifier. The application is built with Streamlit and includes SHAP Explainable AI to interpret model predictions.

---

## 📌 Project Overview

Customer churn is one of the major challenges faced by banks. This project helps identify customers who are likely to leave the bank so that appropriate retention strategies can be implemented.

The application allows users to:

Enter customer details
Predict churn probability
View customer risk level
Receive retention recommendations
Understand prediction explanations using SHAP

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

## 📂 Project Structure
Bank-Churn-App/
│
├── app.py                    # Streamlit application
├── bank_churn_model.cbm      # Trained CatBoost model
├── requirements.txt          # Project dependencies
├── README.md                 # Documentation
└── churn_prediction.ipynb    # Model training notebook

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

---

## 📈 Explainable AI

The project integrates **SHAP (SHapley Additive Explanations)** to explain individual predictions.

The dashboard provides:

* Feature contribution analysis
* SHAP value interpretation
* Natural language explanation of the top contributing features

This improves model transparency and helps understand why a customer is predicted to churn.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/jyotshna068/Bank-Churn-App.git
```

### 2. Navigate to the Project Folder

```bash
cd Bank-Churn-App
```

### 3. Create a Virtual Environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## 📋 Input Features

* Credit Score
* Geography
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Has Credit Card
* Is Active Member
* Estimated Salary

---

## 📤 Output

The application provides:

* Customer Churn Probability
* Risk Category
* Recommended Retention Strategy
* SHAP-based Feature Explanation
* Customer Input Summary

---

## 📈 Explainable AI

The application integrates **SHAP (SHapley Additive Explanations)** to interpret the model's predictions by identifying the features that contribute most to the predicted churn probability.

---

## 🎯 Future Improvements

* FastAPI REST API
* Customer Authentication
* Database Integration
* Prediction History
* Downloadable Prediction Reports
* Email Notifications
* Docker Deployment
* Cloud Deployment (AWS/Azure/GCP)

---

## 👩‍💻 Author

**Jyotshna Devi Gavireddy**

GitHub: https://github.com/jyotshna068

---

## ⭐ If you found this project useful, please consider giving it a star!

```
