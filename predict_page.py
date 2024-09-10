import numpy as np
import pandas as pd
import streamlit as st
import pickle

def load_data():
    with open('loan_status_saved_steps.pkl','rb') as file:
        data = pickle.load(file)
        return data
    
data = load_data()
model = data['model']
    
# [Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome,
 	#LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]


def show_predict_page():

    st.title("Loan Status Prediction")

    Gender,	Married, Dependents = st.columns(3)
    Education, Self_Employed = st.columns(2)
    ApplicantIncome, CoapplicantIncome = st.columns(2)
    LoanAmount, Loan_Amount_Term = st.columns(2)
    Credit_History, Property_Area = st.columns(2)

    gender = ("Male", "Female")
    married = ("Yes", "No")
    edu = ("Graduate", "Not Graduate")
    sel_emp = ("Yes", "No")
    area = ("Rural", "Semiurban", "Urban")

    gender_input = Gender.selectbox("Gender:", gender)
    married_input = Married.selectbox("Married:", married)
    dependents_input = Dependents.text_input("Dependents:")
    edu_input = Education.selectbox("Education:", edu)
    sel_emp_input = Self_Employed.selectbox("Self Employment:", sel_emp)
    app_inc = ApplicantIncome.text_input("Applicant Income:")
    coapp_inc = CoapplicantIncome.text_input("Coapplicant Income:")
    lo_am = LoanAmount.text_input("Loan Amount:")
    lo_am_te = Loan_Amount_Term.text_input("loan Amount term:")
    cre_his = Credit_History.text_input("Credit History:")
    pro_area =  Property_Area.selectbox("Area:",area)

    ok = st.button("Predict")
    if ok:
        user_input = pd.DataFrame({
            'Gender': [gender_input],
            'Married': [married_input],
            'Dependents': [dependents_input],
            'Education': [edu_input],
            'Self_Employed': [sel_emp_input],
            'ApplicantIncome': [app_inc],
            'CoapplicantIncome': [coapp_inc],
            'LoanAmount': [lo_am],
            'Loan_Amount_Term': [lo_am_te],
            'Credit_History': [cre_his],
            'Property_Area': [pro_area]
        })
        
        # convert categorical column in numerical values
        user_input.replace({"Married":{'No':0, 'Yes':1}, 'Gender':{'Male':1, 'Female':0},
                        "Self_Employed":{'No':0, 'Yes':1}, 
                        "Property_Area":{'Rural':0, 'Semiurban':1, 'Urban':2},
                        "Education":{'Graduate':1, 'Not Graduate':0}}, inplace=True)
        
        user_input = user_input.astype(float)

        prediction = model.predict(user_input)
        st.write(f"The predicted loan status is: {'Approved' if prediction[0] == 1 else 'Rejected'}")
show_predict_page()