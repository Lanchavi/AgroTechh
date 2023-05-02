# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 12:23:49 2023

@author: Lanchavi
"""

import numpy as np
import pickle
import streamlit

# loading the saved model
loaded_model = pickle.load(open('C:/ML_rainfall/Rainfall_Prediction.sav','rb'))



#creating a functin for prediction

def rainfall_prediction(input_data)