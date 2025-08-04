import numpy as np
from scipy import stats  # ✅ this is the correct one

data = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55])

# Central Tendency
mean = np.mean(data)
median = np.median(data)
mode_result = stats.mode(data, keepdims=True)  # use keepdims=True for recent versions
mode = mode_result.mode[0]

# Dispersion
data_range = np.ptp(data)  # Peak-to-Peak Range
variance = np.var(data)    # Variance
std_deviation = np.std(data)  # Standard Deviation
iqr = np.percentile(data, 75) - np.percentile(data, 25)  # IQR

# Print the results
print("Central Tendency:")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")

print("\nDispersion:")
print(f"Range: {data_range}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")
print(f"IQR: {iqr}")
