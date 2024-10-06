import numpy as np
import matplotlib.pyplot as plt
from linear_regression import LinearRegression


def generate_linear_data(n_samples=100, noise=10):
    """
    Generates synthetic linear data for regression analysis.

    Args:
        n_samples: The number of samples to generate.
        noise: The standard deviation of the Gaussian noise added to the data.

    Returns:
        A tuple (X, y) where X is the input feature
        matrix and y is the target values.
    """
    np.random.seed(42)  # Set the random seed for reproducibility
    X = 2 * np.random.rand(n_samples, 1)  # Generate random input features
    # Generate target values with noise
    y = 4 + 3 * X + np.random.randn(n_samples, 1) * noise
    return X, y


def main():
    # Generate dummy data
    X, y = generate_dummy_data()

    # Create and train the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Make predictions
    y_pred = model.predict(X)

    # Plot the results
    plt.scatter(X, y, color='blue', label='Actual data')
    plt.plot(X, y_pred, color='red', label='Predicted line')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Linear Regression Example')
    plt.legend()
    plt.show()

    print('y_pred', y_pred[0:5])


# Notify the team about the function name change
# TODO: The function 'gddata' has been renamed to 'generate_linear_data'.
# Please update your references accordingly.

if __name__ == '__main__':
    main()