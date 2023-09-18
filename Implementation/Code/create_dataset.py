import numpy as np
from scipy.stats import multivariate_normal
from sklearn.preprocessing import StandardScaler

# Generating a bivariate dataset with a multivariate normal distribution
def create_bivariate(cov, mean, n_points, seed=101):
    """
    Parameters:
    - cov: Covariance matrix determining the shape and orientation of the distribution.
    - mean: Mean vector specifying the center of the distribution.
    - n_points: Number of data points to generate.
    - seed: Seed for the random number generator (optional).
    Returns:
    - X: Dataset generated from the multivariate normal distribution.
    """
  
    # Defining dataset
    distr = multivariate_normal(cov=cov, mean=mean, seed=seed)
    X = distr.rvs(size=n_points)
    return X

# Standardizing the dataset to ensure that features have zero mean and unit variance.
def standardize_data(X):
    """
    Parameters:
    - X: Input dataset.
    Returns:
    - X_scaled: Standardized dataset.
    """
  
    sc = StandardScaler()
    X_scaled = sc.fit_transform(X)
    return X_scaled
