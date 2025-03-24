import numpy as np
import matplotlib.pyplot as plt

# Given data
samples = np.arange(1, 15)
means = np.array([11, 10.9, 11.5, 11.1, 11.7, 11, 11, 12, 12.4, 11.4, 11.9, 11.8, 12.3, 11.6])
ranges = np.array([2.4, 1.4, 1.7, 0.7, 0.8, 1.1, 2, 2.1, 1.4, 1.2, 0.7, 1, 1.2, 1.5])

# Compute X̄̄ and R̄
X_bar_bar = np.mean(means)
R_bar = np.mean(ranges)

# Control chart constants for n=4
A2 = 0.729
D3 = 0
D4 = 2.282

# Control limits for X̄ chart
UCL_X = X_bar_bar + A2 * R_bar
LCL_X = X_bar_bar - A2 * R_bar

# Control limits for R chart
UCL_R = D4 * R_bar
LCL_R = D3 * R_bar  # LCL_R = 0 since D3 = 0

# Plot X̄ Chart
plt.figure(figsize=(10,5))
plt.plot(samples, means, marker='o', linestyle='-', color='b', label='Sample Means')
plt.axhline(y=X_bar_bar, color='g', linestyle='--', label=f'CL = {X_bar_bar:.3f}')
plt.axhline(y=UCL_X, color='r', linestyle='--', label=f'UCL = {UCL_X:.3f}')
plt.axhline(y=LCL_X, color='r', linestyle='--', label=f'LCL = {LCL_X:.3f}')
plt.xlabel('Sample Number')
plt.ylabel('Mean Weight')
plt.title('X̄ Control Chart')
plt.legend()
plt.grid()
plt.show()

# Plot R Chart
plt.figure(figsize=(10,5))
plt.plot(samples, ranges, marker='o', linestyle='-', color='b', label='Sample Ranges')
plt.axhline(y=R_bar, color='g', linestyle='--', label=f'CL = {R_bar:.3f}')
plt.axhline(y=UCL_R, color='r', linestyle='--', label=f'UCL = {UCL_R:.3f}')
plt.axhline(y=LCL_R, color='r', linestyle='--', label=f'LCL = {LCL_R:.3f}')
plt.xlabel('Sample Number')
plt.ylabel('Range')
plt.title('R Control Chart')
plt.legend()
plt.grid()
plt.show()

# Print calculated values
print(f"X̄̄ = {X_bar_bar:.3f}, UCL_X = {UCL_X:.3f}, LCL_X = {LCL_X:.3f}")
print(f"R̄ = {R_bar:.3f}, UCL_R = {UCL_R:.3f}, LCL_R = {LCL_R:.3f}")