# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 19:58:59 2023

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
    return prediction
#[0]

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
   
 
def main():
   
   
    # giving a title
    st.title('Fertilizer Prediction Web App')
   
   
    # getting the input data from the user
   
   
    Temparature = st.text_input('Temperature')
    if is_float(Temparature):
        Temparature = float(Temparature)
   
    Humidity = st.text_input('Humidity')
    if is_float(Humidity):
        Humidity = float(Humidity)
       
    Moisture = st.text_input('Moisture')
    if is_float(Moisture):
        Moisture = float(Moisture)
       
    Soil_Type = st.text_input('Soil Type')
    if is_float(Soil_Type):
        Soil_Type = float(Soil_Type)
       
    Crop_Type = st.text_input('Crop Type')
    if is_float(Crop_Type):
        Crop_Type = float(Crop_Type)
       
    Nitrogen = st.text_input('Nitrogen')
    if is_float(Nitrogen):
        Nitrogen = float(Nitrogen)
       
    Potassium = st.text_input('Potassium')
    if is_float(Potassium):
        Potassium = float(Potassium)
       
    Phosphorous = st.text_input('Phosphorous')
    if is_float(Phosphorous):
        Phosphorous = float(Phosphorous)
   
   
   
   
   
    # code for Prediction
    label = ''
   
    # creating a button for Prediction
   
    if st.button('Crop prediction'):
        label = fertilizer_prediction([Temparature,Humidity,Moisture,Soil_Type,Crop_Type,Nitrogen,Potassium,Phosphorous])
       
       
    st.success(label)
    #return label
   
   
   
   
   
if __name__ == '__main__':
    main() 
