# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 12:12:59 2023

@author: Anuj Khanvilkar
"""

import numpy as np
import pickle
import streamlit as st
import requests



# loading the saved model
loaded_model = pickle.load(open('C:/ML_crop/trained_model.sav','rb'))




# creating a function for Prediction
def crop_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    return prediction[0]


    
  
def main():
    
    
    # giving a title
    st.title('Crop Prediction Web App')
    
    
    
    # getting the input data from the user
    
    
    N = st.text_input('Nitrogen')
    P = st.text_input('Phosphorous')
    K = st.text_input('Potassium')
    temperature = st.text_input('Temperature')
    humidity = st.text_input('Humidity')
    ph = st.text_input('pH')
    rainfall = st.text_input('Rainfall')
    
    
    
    
    # code for Prediction
    label = ''
    
    # creating a button for Prediction
    
    if st.button('Crop prediction'):
        label = crop_prediction([int(N),int(P),int(K),float(temperature),float(humidity),float(ph),float(rainfall)])
        
        
    st.success(label)
    #return label
    
    #decoration

    
    
if __name__ == '__main__':
    main()