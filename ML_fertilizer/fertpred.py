# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 18:35:05 2023

@author: Lanchavi
"""


import numpy as np
import pickle
import streamlit as st
import sklearn


# loading the saved model
fertilizer_model = pickle.load(open('C:/ML_fertilizer/fertilizer_model.sav','rb'))


# creating a function for Prediction

def fertilizer_prediction(input_data):
   

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = fertilizer_model.predict(input_data_reshaped)
    if prediction[0] == 0:
            return '10-26-26'
    elif prediction[0] == 1:
            return '14-35-14'
    elif prediction[0] == 2:
            return '17-17-17'        
    elif prediction[0] == 3:
            return '20-20'        
    elif prediction[0] == 4:
            return '28-28'        
    elif prediction[0] == 5:
            return 'DAP'
    elif prediction[0] == 6:
            return 'Urea'
           
 
def main():
   
   
    # giving a title
    st.title('Fertilizer Prediction')
   
   
    # getting the input data from the user
   
   
    Temparature = st.text_input('Temperature')
    Humidity = st.text_input('Humidity')
    Moisture = st.text_input('Moisture')
    Soil_Type = st.text_input('Soil Type')
    Crop_Type = st.text_input('Crop Type')
    Nitrogen = st.text_input('Nitrogen')
    Potassium = st.text_input('Potassium')
    Phosphorous = st.text_input('Phosphorous')
   
   
   
   
   
    # code for Prediction
    label = ''
   
    # creating a button for Prediction
   
    if st.button('Fertilizer prediction'):
        label = fertilizer_prediction([float(Temparature),float(Humidity),float(Moisture),str(Soil_Type),str(Crop_Type),float(Nitrogen),float(Potassium),float(Phosphorous)])
       
       
    st.success(label)
    #return label
   
   
   
   
   
if __name__ == '__main__':
    main()