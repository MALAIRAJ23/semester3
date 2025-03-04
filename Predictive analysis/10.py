y1 = [191, 195, 181, 183, 176, 208, 189, 197, 188, 192, 179, 183, 174, 190, 188, 163, 195, 186, 181, 175, 192, 174, 176, 197, 190]
y2 = [155, 149, 148, 153, 144, 157, 150, 159, 152, 150, 158, 147, 150, 159, 151, 137, 155, 153, 145, 140, 154, 143, 139, 167, 163]
x1 = [179, 201, 185, 188, 171, 192, 190, 189, 197, 187, 186, 174, 185, 195, 187, 161, 183, 173, 182, 165, 185, 178, 176, 200, 187]
x2 = [145, 152, 149, 149, 142, 152, 149, 152, 159, 151, 148, 147, 152, 157, 158, 130, 158, 148, 146, 137, 152, 147, 143, 158, 150]
n = len(y1)
# Mean
print(sum(y1))
y1_mean = sum(y1) / n
y2_mean = sum(y2) / n
x1_mean = sum(x1) / n
x2_mean = sum(x2) / n
# Mean vector
mean_vector = [[y1_mean, y2_mean], [x1_mean, x2_mean]]
print("Mean vector:")
print(mean_vector)
# Covariance
# Syy
y11 = [i*i for i in y1]
sy11 = (sum(y11) - n * y1_mean**2) / (n - 1)
y22 = [i*i for i in y2]
sy22 = (sum(y22) - n * y2_mean**2) / (n - 1)
y1y2 = [i*j for i,j in zip(y1, y2)]
sy12 = (sum(y1y2) - n * y1_mean * y2_mean) / (n - 1)
sy21 = sy12  
# Sxy 
y1x1 = [i*j for i,j in zip(y1, x1)]
syx11 = (sum(y1x1) - n * y1_mean * x1_mean) / (n - 1)
y1x2 = [i*j for i,j in zip(y1, x2)]
syx12 = (sum(y1x2) - n * y1_mean * x2_mean) / (n - 1)
y2x1 = [i*j for i,j in zip(y2, x1)]
syx21 = (sum(y2x1) - n * y2_mean * x1_mean) / (n - 1)
y2x2 = [i*j for i,j in zip(y2, x2)]
syx22 = (sum(y2x2) - n * y2_mean * x2_mean) / (n - 1)
# Sxx
x11 = [i*i for i in x1]
sx11 = (sum(x11) - n * x1_mean**2) / (n - 1)
x22 = [i*i for i in x2]
sx22 = (sum(x22) - n * x2_mean**2) / (n - 1)
x1x2 = [i*j for i,j in zip(x1, x2)]
sx12 = (sum(x1x2) - n * x1_mean * x2_mean) / (n - 1)
sx21 = sx12  
cov_matrix = [
    [sy11, sy12, syx11, syx12],
    [sy21, sy22, syx21, syx22],
    [syx11, syx21, sx11, sx12],
    [syx12, syx22, sx12, sx22]
]
print("Covariance Matrix (Syy, Syx, Sxy, Sxx):")
for row in cov_matrix:
    print(row)