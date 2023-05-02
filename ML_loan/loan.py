import numpy as np
import pickle
import streamlit as st
import requests


# loading the saved model
loaded_model = pickle.load(open('C:/ML_loan/trained_model (1).sav','rb'))

# creating a function for Prediction
def crop_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    if prediction[0] == 0:
        return 'The loan status is no'
    else:
        return 'The loan status is yes'
         

    
  
def main():
    
    
    # giving a title
    st.title('Loan Status Prediction ')
    
    
    
    # getting the input data from the user
    #Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,
    
    
    Gender = st.text_input('Gender')
    Married = st.text_input('Married')
    Dependents = st.text_input('Dependents')
    Education = st.text_input('Education')
    Self_Employed = st.text_input('Self Employed')
    ApplicantIncome = st.text_input('Farmer Income')
    CoapplicantIncome = st.text_input('Co-applicant Income')
    LoanAmount = st.text_input('Loan Amount')
    Loan_Amount_Term = st.text_input('Loan_Amount_Term')
    Credit_History = st.text_input('Credit_History')
    Property_Area = st.text_input('Property_Area')
  
    
    
    
    # code for Prediction
    label = ''
    
    # creating a button for Prediction
    
    if st.button('Loan Status prediction'):
        label = crop_prediction([float(Gender),float(Married),float(Dependents),float(Education),float(Self_Employed),float(ApplicantIncome),float(CoapplicantIncome),float(LoanAmount),float(Loan_Amount_Term),float(Credit_History),float(Property_Area)])
     
        # if label == 0:
        #     st.success(label+', The loan status is no')
            
        # else:
        #     st.success(label+', The loan status is yes')
        
        
        
        
        st.success(label)
  #return label
    
    
    
    
if __name__ == '__main__':
    main()