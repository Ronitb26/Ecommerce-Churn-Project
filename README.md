# 🔍 [Customer Churn Prediction & Retention Strategy App](https://ecom-churn.streamlit.app/)

## 📌 Project Overview

This project addresses a crucial challenge in the e-commerce domain — **customer churn prediction**. By leveraging advanced machine learning techniques and data-driven insights, this application enables businesses to:

- **Identify customers likely to churn.**
- **Understand the reasons behind churn risk.**
- **Receive actionable retention strategies** to reduce potential revenue loss.

Built with an intuitive **Streamlit interface**, this solution empowers business and data teams to make informed decisions in real-time.

---

## 🚀 Key Features

### 1. Churn Data Analysis Module
- Perform detailed **exploratory data analysis (EDA)** on customer churn patterns.
- Visualize distributions, correlations, and trends to uncover **key churn drivers**.
- Gain valuable business insights about factors impacting customer retention.

### 2. Churn Prediction & Retention Strategy Module
- Predict the **churn probability** of any individual customer using a trained **ANN**.
- Generate **personalized retention strategies** based on customer-specific data (e.g., Tenure, Satisfaction Score, Order Patterns).
- Explore **feature-level impact** on churn probability to understand the contribution of each factor.

### 3. Feature Impact & Explainability Module
- Utilize **SHAP (SHapley Additive exPlanations)** for in-depth model explainability.
- Visualize **how each feature shifts the churn prediction** probability.
- Empower stakeholders with transparent and interpretable AI-driven decisions.

---

## 🏆 Model Performance

| Metric         | Final Model | Base Model |
|---------------|------------|------------|
| **Recall**    | 99.36%     | 82.12%     |
| **F1-Score**  | 74.83%     | 69.44%     |

- Model: **ANN**
- Evaluation: Stratified Train-Test Split (80-20) with Cross-validation

---

## ⚙️ Tech Stack

- **Languages & Libraries:** Python, Pandas, Scikit-learn, TensorFlow , Keras
- **Web App Development:** Streamlit
- **Model Explainability:** SHAP
- **Visualization:** Matplotlib, Seaborn

---


