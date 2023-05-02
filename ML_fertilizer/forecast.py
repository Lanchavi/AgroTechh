# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 23:38:52 2023

@author: Lanchavi
"""

#!pip install requests
import requests
 
print("\t\tWelcome to the Weather Forecaster!\n\n")
print("Just Enter the City you want the weather report for and click on the button! It's that simple!\n\n")
 
city_name = input("Enter the name of the City : ")
print("\n\n")
 
# Function to Generate Report
def Gen_report(C):
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occurred"
    print(T)
     
Gen_report(city_name)

import streamlit as st
import subprocess

st.title("Terminal Output")

cmd = 'ls -l'
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
output = result.stdout

st.code(output, language='bash')


