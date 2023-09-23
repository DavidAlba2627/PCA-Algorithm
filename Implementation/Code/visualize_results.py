import numpy as np
import matplotlib.pyplot as plt

# Plots the original dataset and the reduced dataset side by side.
def plot_original_and_reduced(X_original, X_reduced, title="Reduced Data Visualization"):
    """
    Parameters:
    - X_original: Original dataset.
    - X_reduced: Reduced dataset after PCA.
    - title: Title for the reduced dataset plot.
    """
  
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    # Plotting original data
    axs[0].scatter(X_original[:, 0], X_original[:, 1], color="mediumseagreen", alpha=0.3, s=70)
    axs[0].set_title("Original Data", fontsize = 18)
    # Plotting reduced data
    axs[1].scatter(X_reduced, np.zeros_like(X_reduced), color="mediumblue", alpha=0.3, s=100)
    axs[1].set_title(title, fontsize = 18)
    plt.show()

# Plots the original dataset with the principal components.
def plot_principal_components(X, components):
    """
    Parameters:
    - X: Original dataset.
    - components: Principal components.
    """
  
    origin = np.array([[0, 0], [0, 0]])  # origin point
    components_scaled = components * np.array([[1.0], [0.5]])  # scaled principal components
    f, axs = plt.subplots(1, 1, figsize=(6, 6))
    axs.scatter(X[:, 0], X[:, 1], s=70, zorder=-1, color="mediumseagreen", alpha=0.3)
    axs.quiver(*origin, components_scaled[:, 0], components_scaled[:, 1], color=['mediumblue', 'firebrick'], scale=2.7, headwidth=4, width=0.013)
    axs.set_title("Principal Components Visualization", fontsize=16)
    plt.show()
