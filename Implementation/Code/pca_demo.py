import numpy as np
import matplotlib.pyplot as plt
from create_dataset import create_bivariate, standardize_data
from pca_function import PCA
from visualize_results import plot_original_and_reduced, plot_principal_components

def main():
    # Create a bivariate dataset
    X = create_bivariate(cov=[[1, 0.9], [0.9, 1]], mean=[0, 0], n_points=350)

    # Standardize the dataset
    X_standardized = standardize_data(X)

    # Apply PCA to reduce the dataset to 1 principal component
    X_reduced, components = PCA(X_standardized, n_components=1)

    # Visualize the original and reduced datasets
    plot_original_and_reduced(X_standardized, X_reduced, title="PCA Reduced Data")

    # Visualize the principal components on the original dataset
    plot_principal_components(X_standardized, components)

if __name__ == "__main__":
    main()
