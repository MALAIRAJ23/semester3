# Sample data (X: independent variable, Y: dependent variable)
X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 5]

# Compute means
n = len(X)
X_mean = sum(X) / n
Y_mean = sum(Y) / n

# Compute slope (b1) and intercept (b0)
numerator = sum((X[i] - X_mean) * (Y[i] - Y_mean) for i in range(n))
denominator = sum((X[i] - X_mean) ** 2 for i in range(n))
b1 = numerator / denominator
b0 = Y_mean - b1 * X_mean

# Regression equation function
def predict(x):
    return b0 + b1 * x

# Example prediction
x_test = 6
print(f"Predicted value for x={x_test}: {predict(x_test)}")

print(f"Linear Regression Equation: y = {b0:.2f} + {b1:.2f}x")