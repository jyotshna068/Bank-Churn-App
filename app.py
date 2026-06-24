import streamlit as st
import pandas as pd
from catboost import CatBoostClassifier

# -----------------------------
# Load model
# -----------------------------
model = CatBoostClassifier()
model.load_model("bank_churn_model.cbm")

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Bank Churn Predictor",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Bank Customer Churn Prediction App")
st.write("Predict whether a customer will leave the bank or not.")

# -----------------------------
# Input UI
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    credit_score = st.number_input("Credit Score", 300, 900, 650)

    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])

    gender = st.selectbox("Gender", ["Male", "Female"])

    age = st.slider("Age", 18, 100, 35)

    tenure = st.slider("Tenure", 0, 10, 5)

with col2:
    balance = st.number_input("Balance", min_value=0.0, value=50000.0)

    num_products = st.selectbox("Number of Products", [1, 2, 3, 4])

    has_card = st.selectbox("Has Credit Card", [0, 1])

    active_member = st.selectbox("Is Active Member", [0, 1])

    salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Churn"):

    # Feature engineering (same as training)
    balance_salary_ratio = balance / (salary + 1)
    tenure_by_age = tenure / (age + 1)
    credit_score_age_ratio = credit_score / (age + 1)
    products_per_tenure = num_products / (tenure + 1)

    # Build dataframe
    input_df = pd.DataFrame([{
        "CreditScore": credit_score,
        "Geography": geography,
        "Gender": gender,
        "Age": age,
        "Tenure": tenure,
        "Balance": balance,
        "NumOfProducts": num_products,
        "HasCrCard": has_card,
        "IsActiveMember": active_member,
        "EstimatedSalary": salary,
        "BalanceSalaryRatio": balance_salary_ratio,
        "TenureByAge": tenure_by_age,
        "CreditScoreAgeRatio": credit_score_age_ratio,
        "ProductsPerTenure": products_per_tenure
    }])

    # -----------------------------
    # FIX: categorical types must be string
    # -----------------------------
    cat_cols = ["Geography", "Gender"]

    for col in cat_cols:
        input_df[col] = input_df[col].astype(str)

    # -----------------------------
    # IMPORTANT: enforce column order (must match training)
    # -----------------------------
    feature_order = [
        "CreditScore",
        "Geography",
        "Gender",
        "Age",
        "Tenure",
        "Balance",
        "NumOfProducts",
        "HasCrCard",
        "IsActiveMember",
        "EstimatedSalary",
        "BalanceSalaryRatio",
        "TenureByAge",
        "CreditScoreAgeRatio",
        "ProductsPerTenure"
    ]

    input_df = input_df[feature_order]

    # -----------------------------
    # Prediction (CORRECT)
    # -----------------------------
    churn_prob = model.predict_proba(input_df)[0][1]

    # -----------------------------
    # Output
    # -----------------------------
    st.subheader("Prediction Result")

    st.metric("Churn Probability", f"{churn_prob:.2%}")

    if churn_prob > 0.80:
        st.error("🔴 High Risk Customer")
        st.write("Recommended Action: Premium Retention Offer")

    elif churn_prob > 0.60:
        st.warning("🟠 Medium Risk Customer")
        st.write("Recommended Action: Relationship Manager Call")

    elif churn_prob > 0.40:
        st.info("🟡 Moderate Risk Customer")
        st.write("Recommended Action: Promotional Campaign")

    else:
        st.success("🟢 Low Risk Customer")
        st.write("Recommended Action: Standard Engagement")

    st.subheader("Customer Input Data")
    st.dataframe(input_df)