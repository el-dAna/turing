import numpy as np


class LinearRegression:
    def __init__(self):
        """
        Initialize the Linear Regression model.
        """
        self.weights = None

    def fit(self, X, y):
        """
        Train the model using the normal equation.

        Parameters:
        X (array): Features.
        y (array): Target.
        """
        # Add an intercept term (bias)
        X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Add x0 = 1 to each instance
        self.weights = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

    def predict(self, X):
        """
        Make predictions using the trained model.

        Parameters:
        X (array): Features for prediction.

        Returns:
        array: Predicted values.
        """
        X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Add x0 = 1 to each instance
        return X_b.dot(self.weights)
