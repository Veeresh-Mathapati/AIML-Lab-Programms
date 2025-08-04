
import numpy as np
import the
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

#Load the required libraries
import pandas as pd
import numpy as np
import seaborn as sns
#Load the data
df = pd.read_csv('titanic.csv')



# View the data
df.head()

# Basic information
df.info()
df.describe()
df.duplicated().sum()
# Unique values
df['Pclass'].unique()
df['Survived'].unique()
df['Sex'].unique()

import pandas as pd
import numpy as np

# Load the Titanic dataset
titanic_df = pd.read_csv('titanic.csv')  # Replace with the actual path to your Titanic dataset

# Display the first few rows of the dataset to understand its structure
print("Sample data:")
print(titanic_df.head())

# Central Tendency for 'Age' and 'Fare' parameters
age_mean = titanic_df['Age'].mean()
age_median = titanic_df['Age'].median()
age_mode = titanic_df['Age'].mode()[0]

fare_mean = titanic_df['Fare'].mean()
fare_median = titanic_df['Fare'].median()
fare_mode = titanic_df['Fare'].mode()[0]

# Dispersion for 'Age' and 'Fare' parameters
age_range = titanic_df['Age'].max() - titanic_df['Age'].min()
age_variance = titanic_df['Age'].var()
age_std_deviation = titanic_df['Age'].std()
age_iqr = titanic_df['Age'].quantile(0.75) - titanic_df['Age'].quantile(0.25)

fare_range = titanic_df['Fare'].max() - titanic_df['Fare'].min()
fare_variance = titanic_df['Fare'].var()
fare_std_deviation = titanic_df['Fare'].std()
fare_iqr = titanic_df['Fare'].quantile(0.75) - titanic_df['Fare'].quantile(0.25)

# Print the central tendency and dispersion for 'Age' and 'Fare'
print("\nCentral Tendency for Age:")
print(f"Mean: {age_mean}")
print(f"Median: {age_median}")
print(f"Mode: {age_mode}")

print("\nDispersion for Age:")
print(f"Range: {age_range}")
print(f"Variance: {age_variance}")
print(f"Standard Deviation: {age_std_deviation}")
print(f"IQR: {age_iqr}")

print("\nCentral Tendency for Fare:")
print(f"Mean: {fare_mean}")
print(f"Median: {fare_median}")
print(f"Mode: {fare_mode}")

print("\nDispersion for Fare:")
print(f"Range: {fare_range}")
print(f"Variance: {fare_variance}")
print(f"Standard Deviation: {fare_std_deviation}")
print(f"IQR: {fare_iqr}")



