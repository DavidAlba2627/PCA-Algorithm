import numpy as np
from numpy.linalg import eig
from sklearn.preprocessing import normalize

# Principal Component Analysis (PCA) implementation
def PCA(X, n_components):
    """
    Parameters:
    - X: Dataset
    - n_components: Number of principal components to retain
    Returns:
    - reduced_dataset: Dataset transformed by PCA
    - eigvectors_sort: Sorted eigenvectors (principal components)
    """
  
    # Calculating matrix of covariance
    cov_matrix = np.cov(X.T)
    # Eigenvectors and eigenvalues
    eigenvalues, eigenvectors = eig(cov_matrix)
    # Sorting eigenvalues in descending order
    sort = np.argsort(eigenvalues)[::-1]
    eigvalues_sort = eigenvalues[sort]
    # Principal Components
    eigvectors_sort = normalize(eigenvectors.T[sort], axis=0)
    # Matrix of transformation
    transformation_matrix = eigvectors_sort.T
    # Applying transformation to original dataset
    reduced_dataset = X @ transformation_matrix[:, 0:n_components]
    
    return reduced_dataset, eigvectors_sort
