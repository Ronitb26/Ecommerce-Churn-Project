import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

st.set_page_config(page_title="Model Insights",layout="wide")
st.markdown("# <p style='text-align: center;'>Model Insights</p>",unsafe_allow_html=True)

with open('6_ecom_v2.csv') as f:
    df = pd.read_csv(f)
X = df.drop(columns=['Churn'])

with open("9_test_data.csv") as f:
    df_test = pd.read_csv(f)
X_test = df_test.drop(columns=['Churn'])

y_test = df_test['Churn']

with open("8_pipeline.pkl",'rb') as file:
    pipeline = pickle.load(file)
model = pipeline.named_steps['model']
transformer = pipeline.named_steps['preprocessor']
importance = model.feature_importances_
features = X.columns
X_test = transformer.transform(X_test)

# Barplot for Feature Imp
fi_df = pd.DataFrame({'Feature': features, 'Importance': importance}).sort_values(by='Importance', ascending=False)
fig, ax = plt.subplots(figsize = (12,6))
sns.barplot(x='Importance', y='Feature', data=fi_df.head(10), ax=ax, palette='viridis')
ax.set_title('Top 10 Feature Importance')
st.pyplot(fig)

# roc curve
from sklearn.metrics import roc_curve,auc
y_proba = model.predict_proba(X_test)[:, 1]  # probability for class 1 (churn)
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)
fig, ax = plt.subplots(figsize=(12,6))
ax.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')  # diagonal line
ax.set_xlim((0.0,1.0))
ax.set_ylim((0.0,1.05))
ax.set_xlabel('False Positive Rate (1 - Specificity)')
ax.set_ylabel('True Positive Rate (Recall)')
ax.set_title('Receiver Operating Characteristic (ROC) Curve')
ax.legend(loc="lower right")
st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    # Confussion Matrix
    from sklearn.metrics import ConfusionMatrixDisplay
    fig, ax = plt.subplots(figsize=(8,5))
    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, cmap='Blues', ax=ax)
    st.pyplot(fig)
with col2:
    st.markdown("""
        <div style='text-align: center;'>
            <h2>📊 Model Performance Metrics</h2>
            <p><b>Accuracy:</b> 0.96</p>
            <p><b>Recall:</b> 0.91</p>
            <p><b>Precision:</b> 0.89</p>
            <p><b>F1 Score:</b> 0.90</p>
            <p><b>ROC AUC:</b> 0.99</p>
        </div>
    """, unsafe_allow_html=True)

