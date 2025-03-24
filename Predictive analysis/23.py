import numpy as np
import matplotlib.pyplot as plt

# Given data
carpets = np.array([1, 2, 3, 4, 5, 6, 7, 8])
defects = np.array([3, 5, 8, 4, 3, 5, 7, 5])
sample_size = 8  # Each carpet is a sample

# Calculate proportion defective (p_i)
p_i = defects / sample_size

# Compute control limits
CL = np.mean(p_i)
sigma_p = np.sqrt((CL * (1 - CL)) / sample_size)
UCL = CL + 3 * sigma_p
LCL = max(0, CL - 3 * sigma_p)  # LCL cannot be negative

# Plot control chart
plt.figure(figsize=(10,5))
plt.plot(carpets, p_i, marker='o', linestyle='-', color='b', label='Proportion Defective')
plt.axhline(y=CL, color='g', linestyle='--', label=f'CL = {CL:.3f}')
plt.axhline(y=UCL, color='r', linestyle='--', label=f'UCL = {UCL:.3f}')
plt.axhline(y=LCL, color='r', linestyle='--', label=f'LCL = {LCL:.3f}')

# Labels and title
plt.xlabel('Carpet Sample Number')
plt.ylabel('Proportion Defective')
plt.title('p-Chart for Woolen Carpets Defects')
plt.legend()
plt.grid()
plt.show()

# Print calculated values
print(f"CL = {CL:.3f}, UCL = {UCL:.3f}, LCL = {LCL:.3f}")