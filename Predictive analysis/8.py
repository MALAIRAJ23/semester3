
data = {
    "y1": [35, 35, 40, 10, 6, 20, 35, 35, 35, 30],
    "y2": [3.5, 4.9, 30.0, 2.8, 2.7, 2.8, 4.6, 10.9, 8.0, 1.6],
    "y3": [2.80, 2.70, 4.38, 3.21, 2.73, 2.81, 2.88, 2.90, 3.28, 3.20]
}

variables = list(zip(data["y1"], data["y2"], data["y3"]))
n = len(variables)


def calculate_mean(values):
    return sum(values) / len(values)


mean_vector = [calculate_mean([row[i] for row in variables]) for i in range(3)]


def calculate_variance(values, mean):
    return sum((x - mean) ** 2 for x in values) / (len(values) - 1)


variances = [
    calculate_variance([row[i] for row in variables], mean_vector[i]) for i in range(3)
]


def calculate_covariance(x_values, y_values, x_mean, y_mean):
    return sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values)) / (len(x_values) - 1)


covariance_matrix = [[
    calculate_covariance(
        [row[i] for row in variables], 
        [row[j] for row in variables], 
        mean_vector[i], 
        mean_vector[j]
    ) for j in range(3)
] for i in range(3)]


print("Mean Vector:", mean_vector)
print("\nVariance:", variances)
print("\nCovariance Matrix:")
for row in covariance_matrix:
    print(row)
