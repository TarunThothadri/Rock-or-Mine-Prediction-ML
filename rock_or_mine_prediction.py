# -*- coding: utf-8 -*-
"""Rock or Mine Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1slGjMSAsbd56pxJfQDNLyPWYAlrl9owJ

Rock or Mine prediction using python

Importing libraries
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and data Processing"""

#load data
sonar_data = pd.read_csv('/content/sonar data.csv',header = None)

sonar_data.head()

sonar_data.tail()

sonar_data.shape

sonar_data.describe()

sonar_data[60].value_counts() #to check whether imbalance data is present

sonar_data.groupby(60).mean()

#seaparate data  and labels
X = sonar_data.drop(columns=60,axis=1)
Y = sonar_data[60]

#Train Test Split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.1,random_state = 1,stratify=Y) #Stratify-split data with almost equal R&M in Y
print(X.shape,X_train.shape,X_test.shape)
print(Y.shape,Y_train.shape,Y_test.shape)

"""Train the model"""

#Train the model
model = LogisticRegression()

model.fit(X_train,Y_train)

"""Evaluation"""

#accuracy on train data
X_train_prediction = model.predict(X_train) #predicting Y
training_data_accuracy = accuracy_score(X_train_prediction,Y_train) #comparing predicted and original value
print("Accuracy on training data : ",training_data_accuracy*100,"%")

#accuracy on test data
X_test_prediction = model.predict(X_test) #predicting Y
testing_data_accuracy = accuracy_score(X_test_prediction,Y_test) #comparing predicted and original value
print("Accuracy on testing data : ",testing_data_accuracy*100,"%")

"""Predictor"""

input_data = (0.0260,0.0363,0.0136,0.0272,0.0214,0.0338,0.0655,0.1400,0.1843,0.2354,0.2720,0.2442,0.1665,0.0336,0.1302,0.1708,0.2177,0.3175,0.3714,0.4552,0.5700,0.7397,0.8062,0.8837,0.9432,1.0000,0.9375,0.7603,0.7123,0.8358,0.7622,0.4567,0.1715,0.1549,0.1641,0.1869,0.2655,0.1713,0.0959,0.0768,0.0847,0.2076,0.2505,0.1862,0.1439,0.1470,0.0991,0.0041,0.0154,0.0116,0.0181,0.0146,0.0129,0.0047,0.0039,0.0061,0.0040,0.0036,0.0061,0.0115)
input_np = np.asarray(input_data)
#Reshape the np array as we predict the model for one instance
input_np_reshaped = input_np.reshape(1,-1)
prediction = model.predict(input_np_reshaped)
if(prediction[0] == 'R'):
  print("It's a ROCK!")
else:
  print("It's a MINE!")

