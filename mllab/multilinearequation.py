X = [[1, 15.57, 2463, 472.92, 18],
    [1, 44.02, 2048, 1339.75, 9.5],
    [1, 20.42, 3940, 620.25, 12.8],
    [1, 18.74, 6505, 568.33, 36.7],
    [1, 49.20, 5723, 1497.60, 35.7],
    [1, 44.92, 11520, 1365.83, 24.0],
    [1, 55.48, 5779, 1687.00, 43.3],
    [1, 59.28, 5769, 1639.92, 46.7],
    [1, 94.39, 8461, 2872.33, 78.7],
    [1, 128.02, 20106, 3655.08, 180.5]] 

y = [566.52, 696.82, 1033.15, 1033.62, 1611.37, 1613.27, 1854.17, 2160.55, 2305.58, 3503.93]

def transpose(matrix):
    result = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        result.append(row)
    return result

def mat_mult(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            sum_val = 0
            for k in range(len(A[0])):
                sum_val += A[i][k] * B[k][j]
            row.append(sum_val)
        result.append(row)
    return result

def inverse(matrix):
    n = len(matrix)
    aug = [matrix[i] + [1 if i == j else 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        diag = aug[i][i]
        for j in range(2 * n):
            aug[i][j] /= diag
        for k in range(n):
            if k != i:
                factor = aug[k][i]
                for j in range(2 * n):
                    aug[k][j] -= factor * aug[i][j]
    return [row[n:] for row in aug]

X_T = transpose(X)
X_T_X = mat_mult(X_T, X)
X_T_y = mat_mult(X_T, [[val] for val in y])
B = mat_mult(inverse(X_T_X), X_T_y)

print("Regression Equation:")

print("Y = {:.4f} + ({:.4f} * X1) + ({:.4f} * X2) + ({:.4f} * X3) + ({:.4f} * X4) ".format(
    B[0][0], B[1][0], B[2][0], B[3][0], B[4][0]
))