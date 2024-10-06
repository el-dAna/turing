import numpy as np


def standardize(X):
    """
    Standardize the features by removing the mean and scaling to unit variance.

    Parameters:
    X (array): Features to standardize.

    Returns:
    array: Standardized features.
    """
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return (X - mean) / std
