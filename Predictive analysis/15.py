import numpy as np

# Given data
x1 = np.array([2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2.0, 1.0, 1.5, 1.1])
x2 = np.array([2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9])         

# Step 1: Create matrix
X = np.column_stack((x1, x2))

# Step 2: Compute the mean of each column
mean_X = np.mean(X, axis=0)

# Step 3: Center the data
X_centered = X - mean_X

# Step 4: Compute covariance matrixb
cov_matrix = np.cov(X_centered, rowvar=False)

# Step 5: Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Step 6: Sort eigenvectors by decreasing eigenvalues
idx = np.argsort(eigenvalues)[::-1]
eigenvectors = eigenvectors[:, idx]
eigenvalues = eigenvalues[idx]

# Step 7: Transform data
X_transformed = X_centered @ eigenvectors

# Output results
print("Mean of X:", mean_X)
print("\nCentered Data:\n", X_centered)
print("\nCovariance Matrix:\n", cov_matrix)
print("\nEigenvalues:", eigenvalues)
print("\nEigenvectors:\n", eigenvectors)
print("\nTransformed Data:\n", X_transformed)