import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import Imputer
import csv


class LinRegression:
    """ Linear Regression class

    Parameters
    ----------
    :param dataset: .csv file

    """

    def __init__(self, dataset):
        self.dataset = dataset

    def fill_na_values(self, data):
        imr = Imputer(missing_values='NaN', strategy='mean', axis=0)
        imr.fit(data)

    def import_and_split_data(self, X_cols1, X_cols2, y_cols):
        """

        Parameters
        ----------
        :param X_cols1: data.iloc[:, X_cols1:X_cols2].values. The
        column to be excluded from the set

        :param X_cols2: data.iloc[:, X_cols1:X_cols2].values. The
        column to be included from the set.

        :param y_cols: data.iloc[:, y_cols].values

        """
        try:
            data = pd.read_csv(self.dataset, header=None)

            # Split the data into X and y
            X = data.iloc[:, X_cols1:X_cols2].values
            y = data.iloc[:, y_cols].values
            imr = Imputer(missing_values='NaN', strategy='mean', axis=0)
            imr.fit(X)
            imr.fit(y)

            # Use train_test_split to create our training and test sets
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        except UnicodeDecodeError:
            print('utf-8 codec cant decode byte: invalid continuation byte')
        finally:
            data = pd.read_csv(self.dataset, header=None, encoding='latin-1')

            # Split the data into X and y
            X = data.iloc[:, X_cols1:X_cols2].values
            y = data.iloc[:, y_cols].values
            imr = Imputer(missing_values='NaN', strategy='mean', axis=0)
            imr.fit(X)
            imr.fit(y)

            # Use train_test_split to create our training and test sets
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    def find_set_shape(self):
        X_train_shape = self.X_train.shape
        X_test_shape = self.X_test.shape
        y_train_shape = self.y_train.shape
        y_test_shape = self.y_test.shape

        # Reshape the data to ensure the Linear Regression model will get
        # created successfully
        self.X_train = self.X_train.reshape(X_train_shape)
        self.y_train = self.y_train.reshape(y_train_shape)
        self.X_test = self.X_test.reshape(X_test_shape)
        self.y_test = self.y_test.reshape(y_test_shape)

    def fit_test_and_predict_results(self):
        self.regressor = LinearRegression()
        self.regressor.fit(self.X_train, self.y_train)

        # Predicting the Test set results
        y_pred = self.regressor.predict(self.X_test)

    def plot_results(self, title, xlabel, ylabel):
        fig, axes = plt.subplots()
        axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
        
        # Plotting the Training set results
        axes1.scatter(self.X_train, self.y_train, color='red')
        axes1.plot(self.X_train, self.regressor.predict(self.X_train), color='blue')
        axes1.title(title)
        axes1.xlabel(xlabel)
        axes1.ylabel(ylabel)
        axes1.show()

        # Plotting the Test set results
        axes2.scatter(self.X_test, self.y_test, color='red')
        axes2.plot(self.X_train, self.regressor.predict(self.X_train), color='blue')
        axes2.title(title)
        axes2.xlabel(xlabel)
        axes2.ylabel(ylabel)
        axes2.show()
