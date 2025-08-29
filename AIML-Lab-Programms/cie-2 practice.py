import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import stats

df=sns.load_dataset("titanic")
print(df.info())
print(df['fare'].describe())
print(df['age'].describe())
print(df.head(10))

sns.countplot(x="pclass", hue="survived", data=df)

plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.title("Survival Count by Passenger Class")
plt.show()


print(df.isnull().sum())
df['age']=df['age'].fillna(df['age'].mean())
print(df.isnull().sum())

# --- Z-Score Outlier Detection ---
z_scores = np.abs(stats.zscore(df["Values"]))
threshold = 3
outliers = df[z_scores > threshold]
print("Outliers:\n", outliers)

# --- Boxplot Visualization ---
sns.boxplot(x=df["Values"])
plt.title("Boxplot of Values (Outliers shown as points)")
plt.show()
