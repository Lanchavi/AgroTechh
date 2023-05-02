# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import metrics
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/ML_rainfall/Rainfall_Prediction.sav','rb'))

#data = pd.read_csv("rainfall in india 1901-2015.csv")
#df=data.melt(['YEAR']).reset_index()
#X=np.asanyarray(df[['Year','Month']]).astype('int')
#y=np.asanyarray(df['Avg_Rainfall']).astype('int')
#print(X.shape)
#print(y.shape)

# splitting the dataset into training and testing
#from sklearn.model_selection import train_test_split

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

from sklearn.ensemble import RandomForestRegressor
loaded_model = RandomForestRegressor(max_depth=100, max_features='sqrt', min_samples_leaf=4,
                      min_samples_split=10, n_estimators=800)
#loaded_model.fit(X_train, y_train)
#y_train_predict=loaded_model.predict(X_train)
#y_test_predict=loaded_model.predict(X_test)
#print("-----------Training Accuracy------------")
#print(round(loaded_model.score(X_train,y_train),3)*100)
#print("-----------Testing Accuracy------------")
#print(round(loaded_model.score(X_test,y_test),3)*100)
predicted = loaded_model.predict([[2016,11]])
predicted