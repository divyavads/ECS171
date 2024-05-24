### SVM MODEL ###

# Challenge: too many variables, SVM best for comparing 2 specific features

'''
refered to: https://scikit-learn.org/stable/modules/svm.html
and https://www.geeksforgeeks.org/support-vector-machine-algorithm/
'''

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split  #library to split test/train data
from sklearn import svm  #library for SVM


# load dataset
df = pd.read_csv('healthcare-dataset-stroke-data.csv')

# drop 'id' column
df = df.drop(columns=['id'])

#display head of csv file (just to visualize)
print(df.head())

#fixing categories w/ non-number entries
categories = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
df = pd.get_dummies(df, columns=categories)

# Fill missing vals of bmi with mean
df['bmi'] = df['bmi'].fillna(df['bmi'].mean())

#display head of csv file (just to visualize)
print(df.head())

# define X (data) and y (target)
X = df.drop(columns=['stroke'])  #input data = all features EXCEPT STROKE
y = df['stroke']  #target variable = stroke 

#split into training and test data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#intializing model
model = svm.SVC()

#fit model with training data
model.fit(X_train, y_train)

#make predictions with test data
y_pred = model.predict(X_test)