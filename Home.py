import streamlit as st

st.set_page_config(page_title="About Project", page_icon="🛍️", layout="wide")

st.markdown("""
# <p style='text-align: center;'>🔍 Predictive Churn Modeling with Business Strategies</p>

## 📌 Project Overview
This project aims to tackle one of the most critical challenges in the e-commerce domain — **customer churn**.
By leveraging machine learning models and data-driven insights, this app helps businesses identify customers 
likely to churn and provides actionable retention strategies to reduce potential revenue loss.

---

## 🚀 Key Features

### 1. [Churn Data Analysis Module](https://ecom-churn.streamlit.app/Churn_Analysis)
- Provides in-depth analysis of churn across the entire dataset.
- Visualizes trends, distributions, and correlations to help businesses understand key churn drivers.

### 2. [Churn Prediction & Retention Strategy Module](https://ecom-churn.streamlit.app/Churn_Prediction)
- Predicts the **churn probability** of an individual customer.
- Generates **personalized retention recommendations** based on customer-specific attributes such as Tenure, 
  Satisfaction Score, Order Patterns, and more.
- Allows users to explore **feature-level impact** on churn probability and see **how each feature shifts the 
  predicted probability from its base value**.

### 3. [Feature Impact & Explainability Module](https://ecom-churn.streamlit.app/Model_Insights)
- Uses **SHAP (SHapley Additive exPlanations)** to explain the impact of features on the model’s churn prediction.
- Helps stakeholders interpret why certain customers are at a higher risk of churn.

---

## 🏆 Model Performance

- **Selected Model:** XGBoost Classifier
- **Accuracy:** 95.56% (Base Model : 95.46%)
- **Recall:** 90.80% (Base Model : 82.12%)
- **F1-Score:** 89.77% (Base Model : 85.44%)

---

## ⚙️ Technologies Used

- **Python, Pandas, Scikit-learn, XGBoost**
- **Streamlit (for Web App Development)**
- **SHAP (for Model Explainability)**
- **Seaborn & Matplotlib (for Visualization)**

---

## 👤 About the Developer

Developed by **[Ronit Balani]("https://www.linkedin.com/in/ronit-balani-845459258/")**, this app demonstrates the practical integration of machine learning, model interpretability, and dashboards for real-world business challenges.

---
""",unsafe_allow_html=True)
