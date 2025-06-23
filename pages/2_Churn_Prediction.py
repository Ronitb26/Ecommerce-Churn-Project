import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Churn Prediction",layout="wide")

with open("6_ecom_v2.csv") as f:
    df = pd.read_csv(f)
with open("8_pipeline.pkl", "rb") as f:
    pipeline = pickle.load(f)
X = df.drop(["Churn"], axis=1)

st.header("Enter Customer Data")
# input data
city_tier = st.slider("Select City Tier",1,3,1)
satisfaction = st.slider("Select Satisfaction Score", 1, 5, 3)
tenure = st.number_input("Enter Tenure in months")
distance = st.number_input("Enter Warehouse to home distance")
devices = st.number_input("Enter number of devices registered")
addresses = st.number_input("Enter number of Addresses")
hike = st.number_input("Enter Order Amount Hike from last year")
count = st.number_input("Enter Number of Orders")
last_order = st.number_input("Enter Days since last order")
cashback = st.number_input("Enter cashback amount")
payment_mode = st.selectbox("Select Customers preferred Payment Mode",X['PreferredPaymentMode'].unique().tolist())
order_cat = st.selectbox("Select Preferred Order Category",X['PreferedOrderCat'].unique().tolist())
marital_status = st.selectbox("Select Marital Status",X['MaritalStatus'].unique().tolist())
if st.checkbox("Ever Registered Complain Before?"):
    complain='Yes'
else:
    complain='No'
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

col1, col2 = st.columns(2)
with col1:
    if st.button("Predict"):
        st.session_state.button_clicked = True
    # form dataframe
    data = [[tenure,city_tier,distance,payment_mode,devices,order_cat,satisfaction,marital_status,addresses,
             complain,hike,count,last_order,cashback]]
    columns = X.columns.tolist()
    test_df = pd.DataFrame(data, columns=columns)
    # Predict
    pipe = pipeline.predict(test_df)
    prob = pipeline.predict_proba(test_df)[0][1]*100
    st.text("Churn Probability : {} %".format(f"{prob:.2f}"))
    if pipe==0:
        st.success("**The Customer will probably stay**")
    else:
        st.warning("**The Customer will probably not stay**")
        if tenure>=10:
            st.info("Provide loyalty benefits for longer tenure to this customer like exclusive deals and priority supports")
        if complain=='Yes':
            st.info("Try to solve the complain placed by customer")
        if addresses>=4:
            st.info("Offer free delivery or address-specific promotions to reduce friction as this customer has more addresses")
        if last_order>5:
            st.info("Run 'We Miss You' email/SMS push campaigns or time-sensitive discount offers to reactivate this customer")
        if satisfaction<=2:
            st.info("Proactively ask for feedback and offer personalized solutions or benefits to improve this customer's satisfaction")
        if distance>=20:
            st.info("optimize delivery promises or offer express delivery upgrades.")
        payment_offer = "Provide personalized payment offers on {} to suit their preference.".format(payment_mode)
        st.info(payment_offer)
with col2:
    if st.session_state.button_clicked==True:
        data = [[tenure, city_tier, distance, payment_mode, devices, order_cat, satisfaction, marital_status, addresses,
                 complain, hike, count, last_order, cashback]]
        columns = X.columns.tolist()
        test_df = pd.DataFrame(data, columns=columns)
        # Predict
        st.subheader("Change in probability with feature")
        ft = st.selectbox("Select Feature",X.columns.tolist())
        if ft in test_df.select_dtypes('number').columns:
            val = st.slider("Select Value",min(X[ft]),max(X[ft]))
        else:
            val = st.selectbox("Select Value",X[ft].unique().tolist())
        test_df[ft]=val
        new_prob = (pipeline.predict_proba(test_df)[0][1]* 100)
        change_prob = (pipeline.predict_proba(test_df)[0][1]* 100)-prob
        st.metric(label = "Churn Probability : ",value ="{} %".format(round(float(new_prob),2)),
                  delta="{} %".format(round(float(change_prob),2)),border=True )


