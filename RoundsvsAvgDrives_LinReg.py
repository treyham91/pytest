# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 23:09:23 2018

@author: treyh
"""
# This plot uses the AvgDrives.csv file located in this repo

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3 as sql

drives_data = pd.read_csv('AvgDrives.csv', header=None)
X = drives_data.iloc[:, 3].values
y = drives_data.iloc[:, 4].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

X_train = X_train.reshape((169,1))
y_train = y_train.reshape((169,1))
X_test = X_test.reshape((43,1))
y_test = y_test.reshape((43,1))

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Total Rounds vs Driving Distance')
plt.xlabel('Total Rounds')
plt.ylabel('Avg Drive')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Total Rounds vs Driving Distance')
plt.xlabel('Total Rounds')
plt.ylabel('Avg Drive')
plt.show()
