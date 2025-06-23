import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(page_title="Churn Analysis",layout="wide")
st.markdown("# <p style='text-align: center;'>Churn Analysis</p>",unsafe_allow_html=True)

with open("4_ecom_v1.csv") as file:
    df = pd.read_csv(file)

# Barplot for Preferred payment mode
col1, col2 = st.columns(2)
with col1:
    churn_p = df[df['Churn'] == 1].groupby('PreferredPaymentMode')['Churn'].count().reset_index()
    churn_p['Churn'] = round(churn_p['Churn'] * 100 / churn_p['Churn'].sum(), 2)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='Churn', y='PreferredPaymentMode', hue='PreferredPaymentMode', data=churn_p, palette='viridis',
                ax=ax, dodge=False, legend=False)
    ax.set_title('Churn Percentage by Payment Method')
    ax.set_xlabel('Churn Percentage (%)')
    ax.set_ylabel('Payment Method')
    st.pyplot(fig)
with col2:
    st.markdown("""
        ### 📊 Observation: Payment Method vs Churn

    - **High-churn segments (Debit & Credit Card)** should be prioritized for targeted offers, discounts, or 
    loyalty programs.
    - **UPI and COD users** demonstrate stronger loyalty — current strategies for these groups seem effective.
    - Consider introducing **wallet-specific promotions** to boost retention for E-Wallet users.
    """)

# Kde plot for Tenure
col3, col4 = st.columns(2)
with col3:
    fig, ax = plt.subplots(figsize=(8.5,5))
    sns.kdeplot(df[df['Churn'] == 1]['Tenure'], label='Churned', fill=True, ax=ax)
    sns.kdeplot(df[df['Churn'] == 0]['Tenure'], label='Retained', fill=True, ax=ax)
    ax.set_xlim(-5, 40)
    ax.set_title('Distribution of Tenure by Churn Status')
    ax.set_xlabel('Tenure')
    ax.set_ylabel('Density')
    ax.legend()
    st.pyplot(fig)
with col4:
    st.markdown("""
    ### 📊 Observation: Tenure vs Churn

    - Customers are most vulnerable to churn within their first 1-3 months of tenure.
    - Early intervention strategies such as onboarding support, incentives, and personalized communication 
    should target this critical period.
    - Long-tenure customers show higher retention likelihood, indicating that existing loyalty measures are 
    effective for this segment.
    """)

# Stacked bar plot for gender
col5, col6 = st.columns(2)
with col5:
    ct = pd.crosstab(df['Gender'], df['Churn'])
    fig, ax = plt.subplots(figsize=(8, 5))
    ct.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], ax=ax)
    ax.set_title('Churn Count by Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Count')
    ax.legend(title='Churn', labels=['No Churn', 'Churn'])
    st.pyplot(fig)
with col6:
    st.markdown("""
    ### 📊 Observation: Gender vs Churn
    
    - Although **male customers account for more churns**, the **relative churn rate** across genders appears 
    similar.
    - The data suggests that gender alone may not be the root cause, but **retention strategies could still be 
    gender-sensitive**.
    """)

# Heatmap for Marital status
col7, col8 = st.columns(2)
with col7:
    cross = pd.crosstab(df['MaritalStatus'], df['Churn'])
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(cross, annot=True, fmt='d', ax=ax)
    ax.set_title('Marital Status vs Churn')
    st.pyplot(fig)
with col8:
    st.markdown("""
    ### 📊 Observation: Marital Status vs Churn
    
    - **Single customers exhibit the highest relative churn rate**, indicating they may be less committed or 
    more price-sensitive.
    - **Retention strategies** should be focused more on **single and divorced** segments, possibly targeting 
    flexibility, incentives, or personalization.
    - **Married customers** show the most loyalty, and strategies here could focus on **rewarding long-term 
    engagement**.
    """)

# Violin plot for WarehouseToHome and complaint
col9, col10 = st.columns(2)
with col9:
    fig, ax = plt.subplots()
    sns.violinplot(x='Churn',y='WarehouseToHome',data=df,hue='Complain',split=True,inner=None,ax=ax)
    ax.set_title('Warehouse to Home Distance vs Churn')
    ax.set_ylabel('Warehouse to Home Distance')
    st.pyplot(fig)
with col10:
    st.markdown("""
    ### 📊 Observation: Warehouse to Home Distance vs Churn (Split by Complaint)
    
    - The combination of **longer delivery distances** and **customer complaints** appears to **correlate with higher churn risk**.
    - Offer some **discounts** on delivery charges for long delivery distances. 
    - Offer **follow-up engagement or resolution feedback forms** for users who file complaints.
    - Consider optimizing **delivery logistics or communication** for users in far-off locations to reduce dissatisfaction.
    """)

# Barplot for preferred Order Category
col11, col12 = st.columns(2)
with col11:
    churn_p = df[df['Churn'] == 1].groupby('PreferedOrderCat')['Churn'].count().reset_index()
    churn_p['Churn'] = round(churn_p['Churn'] * 100 / churn_p['Churn'].sum(), 2)

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='Churn', y='PreferedOrderCat', hue='PreferedOrderCat', data=churn_p, palette='magma', ax=ax,
                dodge=False, legend=False)
    ax.set_title('Churn Percentage by preferred ordered category')
    ax.set_xlabel('Churn Percentage (%)')
    ax.set_ylabel('Preferred Order Category')
    st.pyplot(fig)
with col12:
    st.markdown("""
    ### 📊 Observation: Preferred Order Category vs Churn
    
    - **High churn in electronics (Phone, Laptop & Accessory)** highlights a potential issue in product reliability, support, or delivery experience.
    - **Retention efforts should prioritize tech-focused buyers**, offering personalized support, improved after-sales service, or loyalty programs.
    - **Lower churn in everyday categories (Grocery, Others)** may be leveraged as a stable customer base for cross-promotion or upselling.
    """)

#Stacked barplot for City tier
col13, col14 = st.columns(2)
with col13:
    ct = pd.crosstab(df['CityTier'], df['Churn'])
    fig, ax = plt.subplots(figsize=(8, 5))
    ct.plot(kind='bar', stacked=True, ax=ax,color=['lightgreen', 'salmon'])
    ax.set_title('Churn Count by City Tier')
    ax.set_xlabel('City Tier')
    ax.set_ylabel('Count')
    ax.legend(title='Churn', labels=['No Churn', 'Churn'])
    st.pyplot(fig)
with col14:
    st.markdown("""
    ### 📊 Observation: City Tier vs Churn
    
    - **City Tier 1** requires efforts in **scale-efficient retention**—automation, customer support optimization, and loyalty programs.
    - **City Tier 3** may benefit from **localized engagement**, better fulfillment logistics, and trust-building initiatives.
    - **City Tier 2** presents an **opportunity for growth**, as it shows high stability with untapped potential.
    """)
