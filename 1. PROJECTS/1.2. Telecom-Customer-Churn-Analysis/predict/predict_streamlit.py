# predict by streamlit
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title='Customer Churn Prediction', layout='wide')
# Load the trained model
model = joblib.load('model/logistic_model.pkl')
# Define the input fields for the user
st.title('Dự đoán khách hàng rời đi của công ty Telco')
contract = st.selectbox('Contract Type', ['Month-to-month', 'One year', 'Two year'])
tenure = st.number_input('Tenure (months)', min_value=0, max_value=100, value=0)
online_security = st.selectbox('Online Security', ['Yes', 'No'])
tech_support = st.selectbox('Tech Support', ['Yes', 'No'])
monthly_charges = st.number_input('Monthly Charges', min_value=0.0, value=0.0)
# Create a DataFrame for the input data
input_data = pd.DataFrame({
    'Contract': [contract],
    'tenure': [tenure],
    'OnlineSecurity': [online_security],
    'TechSupport': [tech_support],
    'MonthlyCharges': [monthly_charges]
})
# Preprocess the input data (you may need to encode categorical variables)
input_data['Contract'] = input_data['Contract'].map({'Month-to-month': 0, 'One year': 1, 'Two year': 2})
input_data['OnlineSecurity'] = input_data['OnlineSecurity'].map({'Yes': 1, 'No': 0})
input_data['TechSupport'] = input_data['TechSupport'].map({'Yes': 1, 'No': 0})
# Make a prediction using the loaded model
if st.button('Predict'):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.write('Khách hàng có khả năng sẽ rời đi.')
    else:
        st.write('Khách hàng có khả năng trung thành.')