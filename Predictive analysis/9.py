y1 = [47.8, 46.4, 46.3, 45.1, 47.6, 52.5, 51.2, 49.8, 48.1, 45.0, 51.2, 48.5, 52.1, 48.2, 49.6, 50.7, 47.2, 53.3, 46.2, 46.3]
y2 = [48.8, 47.3, 46.8, 45.3, 48.5, 53.2, 53.0, 50.0, 50.8, 47.0, 51.4, 49.2, 52.8, 48.9, 50.4, 51.7, 47.7, 54.6, 47.5, 47.6]
y3 = [49.0, 47.7, 47.8, 46.1, 48.9, 53.3, 54.3, 50.3, 52.3, 47.3, 51.6, 53.0, 53.7, 49.3, 51.2, 52.7, 48.4, 55.1, 48.1, 51.3]
y4 = [49.7, 48.4, 48.5, 47.2, 49.3, 53.7, 54.5, 52.7, 54.4, 48.3, 51.9, 55.5, 55.0, 49.8, 51.8, 53.3, 49.5, 55.3, 48.4, 51.8]
n = 20

# Mean
y1_mean = sum(y1) / len(y1)
y2_mean = sum(y2) / len(y2)
y3_mean = sum(y3) / len(y3)
y4_mean = sum(y4) / len(y4)

# Variance-Covariance
y11 = [i * i for i in y1]
s11 = (sum(y11) - n * y1_mean**2) / (n - 1)
y22 = [i * i for i in y2]
s22 = (sum(y22) - n * y2_mean**2) / (n - 1)
y33 = [i * i for i in y3]
s33 = (sum(y33) - n * y3_mean**2) / (n - 1)
y44 = [i * i for i in y4]
s44 = (sum(y44) - n * y4_mean**2) / (n - 1)
y12 = [i * j for i, j in zip(y1, y2)]
s12 = (sum(y12) - n * y1_mean * y2_mean) / (n - 1)
y23 = [i * j for i, j in zip(y2, y3)]
s23 = (sum(y23) - n * y2_mean * y3_mean) / (n - 1)
y13 = [i * j for i, j in zip(y1, y3)]
s13 = (sum(y13) - n * y1_mean * y3_mean) / (n - 1)
y14 = [i * j for i, j in zip(y1, y4)]
s14 = (sum(y14) - n * y1_mean * y4_mean) / (n - 1)
y24 = [i * j for i, j in zip(y2, y4)]
s24 = (sum(y24) - n * y2_mean * y4_mean) / (n - 1)
y34 = [i * j for i, j in zip(y3, y4)]
s34 = (sum(y34) - n * y3_mean * y4_mean) / (n - 1)

# Covariance Matrix
covariance_matrix = [
    [s11, s12, s13, s14],
    [s12, s22, s23, s24],
    [s13, s23, s33, s34],
    [s14, s24, s34, s44]
]

# Correlation Matrix
d =[s11*0.5, s22*0.5, s33*0.5, s44*0.5]

d_inverse = [[1 / d[i] if i == j else 0 for j in range(len(d))] for i in range(len(d))]
sdinv = [[sum(covariance_matrix[i][k] * d_inverse[k][j] for k in range(len(d))) for j in range(len(d))] for i in range(len(d))]
r = [[sum(d_inverse[i][k] * sdinv[k][j] for k in range(len(d))) for j in range(len(d))] for i in range(len(d))]
print("Covariance Matrix:")
for row in covariance_matrix:
    print(row)

print("Correlation Matrix:")
for row in r:
    print(row)