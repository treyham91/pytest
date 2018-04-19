import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


class LinRegression:
    """ Linear Regression class

    Parameters
    ----------
    dataset: .csv file, or a data structure that can be imported
    as a table
    """

    def __init__(self, dataset):
        self.dataset = dataset

    def import_and_split_data(self):
        data = pd.read_csv(self.dataset, header=None)
        # Trying to figure out how I can handle splitting the data without having
        # to hard code values for iloc
        X = data.iloc[:, 2:3].values
        y = data.iloc[:, 4].values
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state= 0)

    def find_set_shape(self):
        X_train_shape = self.X_train.shape
        X_test_shape = self.X_test.shape
        y_train_shape = self.y_train.shape
        y_test_shape = self.y_test.shape

        # Reshape the data to ensure the Linear Regression model will get
        # created successfully
        self.X_train = self.X_train.reshape(X_train_shape)
        self.y_train = self.y_train.reshape(y_train_shape)
        self.X_test = self.X_test .reshape(X_test_shape)
        self.y_test = self.y_test.reshape(y_test_shape)

    def fit_test_and_predict_results(self):
        self.regressor = LinearRegression()
        self.regressor.fit(self.X_train, self.y_train)

        # Predicting the Test set results
        y_pred = self.regressor.predict(self.X_test)

    def plot_labels(self, title, xlabel, ylabel):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel


    def plot_results(self):
        # Visualising the Training set results
        plt.scatter(self.X_train, self.y_train, color='red')
        plt.plot(self.X_train, self.regressor.predict(self.X_train), color='blue')
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()

        # Visualising the Test set results
        plt.scatter(self.X_test, self.y_test, color='red')
        plt.plot(self.X_train, self.regressor.predict(self.X_train), color='blue')
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.show()