import pandas as pd
df = pd.DataFrame({'score': [78, 85, 90, 95, 88, 76, 92]})
print(df.describe())

df2=pd.DataFrame({'gender':['M','F','F','M','M','F','M'],
                  'marks':[30,50,70,80,90,40,30]})

df3 = pd.DataFrame({'category':['1','2''3','4','5','6','7']})
print(df.describe())

import seaborn as sns
import matplotlib.pyplot as plt
sns.histplot(df['score'], kde=True)
plt.show()

sns.boxplot(x='gender', y='marks', data=df2)
plt.title("Marks by Gender")
plt.show()

import seaborn as sns
sns.countplot(x='category', data=df3)
plt.show()

df.info()
df.describe(include='all')

df4 = pd.DataFrame({'age':['12','28''30','45','54','62','77']})
print(df4['age'].describe())

sns.histplot(df, kde=True, bins=30)
plt.title("Age Distribution of Passengers")
plt.show()

sns.boxplot(x='gender', y='age', data=df)
plt.title("Age Distribution by Gender")
plt.show()