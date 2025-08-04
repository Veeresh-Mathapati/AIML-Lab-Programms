
# 1. Bar Chart
import matplotlib.pyplot as plt
categories = ['Category A', 'Category B', 'Category C']
amounts = [25, 50, 30]
plt.bar(categories, amounts)
plt.xlabel('Categories')
plt.ylabel('Amounts')
plt.title('Bar Chart of Amounts by Category')
plt.show()

# 2. Pie Chart
categories = ['Category A', 'Category B', 'Category C']
amounts = [25, 50, 30]
plt.pie(amounts, labels=categories, autopct='%1.1f%%')
plt.title('Pie Chart of Amounts by Category')
plt.show()

# 3. Line Chart
years = [2010, 2011, 2012, 2013, 2014]
amounts = [100, 120, 140, 110, 150]
plt.plot(years, amounts, marker='o', linestyle='-')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Line Chart of Amounts Over Time')
plt.grid(True)
plt.show()

# 4. Scatter Plot
x = [10, 20, 30, 40, 50]
y = [50, 40, 30, 20, 10]
plt.scatter(x, y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Scatter Plot of X vs. Y')
plt.grid(True)
plt.show()

# 5. Histogram
import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=20, edgecolor='k')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Data')
plt.show()

# 6. Histogram (Normal Distribution)
mu, sigma = 0, 1
data = np.random.normal(mu, sigma, 1000)
plt.hist(data, bins=30, edgecolor='k', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of a Normal Distribution')
plt.grid(True)
plt.show()

# 7. Histogram (Uniform Distribution)
low, high = 0, 10
data = np.random.uniform(low, high, 1000)
plt.hist(data, bins=20, edgecolor='k', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of a Uniform Distribution')
plt.grid(True)
plt.show()

# 8. Histogram (Exponential Distribution)
scale = 1.0
data = np.random.exponential(scale, 1000)
plt.hist(data, bins=20, edgecolor='k', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of an Exponential Distribution')
plt.grid(True)
plt.show()

# 9. KDE Plot
import seaborn as sns
mu, sigma = 0, 1
data = np.random.normal(mu, sigma, 1000)
sns.kdeplot(data, fill=True)
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Kernel Density Estimation (KDE) Plot of a Normal Distribution')
plt.show()

# 10. Box Plot Comparison
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1, 1000)
sns.boxplot(data=[data1, data2])
plt.xlabel('Distribution')
plt.ylabel('Value')
plt.title('Box Plot Comparison of Two Distributions')
plt.show()

# 11. Pie Chart for Proportions
categories = ['Category A', 'Category B', 'Category C']
proportions = [0.4, 0.3, 0.3]
plt.pie(proportions, labels=categories, autopct='%1.1f%%')
plt.title('Pie Chart of Proportions')
plt.show()

# 12. Stacked Bar Chart
proportions1 = [0.2, 0.4, 0.1]
proportions2 = [0.3, 0.2, 0.4]
plt.bar(categories, proportions1, label='Group 1')
plt.bar(categories, proportions2, bottom=proportions1, label='Group 2')
plt.xlabel('Categories')
plt.ylabel('Proportions')
plt.title('Stacked Bar Chart of Proportions')
plt.legend()
plt.show()

# 13. Horizontal Bar Chart
plt.barh(categories, proportions)
plt.xlabel('Proportions')
plt.ylabel('Categories')
plt.title('Horizontal Bar Chart of Proportions')
plt.show()

# 14. Stacked Area Chart
years = [2010, 2011, 2012, 2013, 2014]
proportions1 = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
proportions2 = np.array([0.2, 0.3, 0.4, 0.5, 0.6])
plt.stackplot(years, proportions1, proportions2, labels=['Group 1', 'Group 2'], alpha=0.5)
plt.xlabel('Year')
plt.ylabel('Proportions')
plt.title('Stacked Area Chart of Proportions Over Time')
plt.legend(loc='upper left')
plt.show()

# 15. Grouped Bar Chart
labels = ['A', 'B', 'C']
x = np.arange(len(labels))
values1 = [20, 35, 30]
values2 = [25, 32, 34]
width = 0.35
fig, ax = plt.subplots()
ax.bar(x - width/2, values1, width, label='Group 1')
ax.bar(x + width/2, values2, width, label='Group 2')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Values')
ax.set_title('Grouped Bar Chart')
ax.legend()
plt.show()


# 15. Grouped Bar Chart
import matplotlib.pyplot as plt
import numpy as np
labels = ['A', 'B', 'C']
x = np.arange(len(labels))
values1 = [20, 35, 30]
values2 = [25, 32, 34]
width = 0.35
fig, ax = plt.subplots()
ax.bar(x - width/2, values1, width, label='Group 1')
ax.bar(x + width/2, values2, width, label='Group 2')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Values')
ax.set_title('Grouped Bar Chart')
ax.legend()
plt.show()

# 16. Heatmap
import seaborn as sns
import numpy as np
corr_matrix = np.corrcoef(np.random.randn(100, 5).T)
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

# 17. Pair Plot
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['species'] = pd.Categorical.from_codes(data.target, data.target_names)
sns.pairplot(df, hue='species')
plt.show()

# 18. Time Series Line Chart
import pandas as pd
import matplotlib.pyplot as plt
dates = pd.date_range('20210101', periods=100)
data = pd.Series(np.random.randn(100).cumsum(), index=dates)
data.plot()
plt.title('Time Series Line Chart')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()

# 19. Area Chart of Time Series
import matplotlib.pyplot as plt
data = np.random.rand(10).cumsum()
plt.fill_between(range(10), data, color='skyblue', alpha=0.4)
plt.plot(data, color='Slateblue', alpha=0.6)
plt.title('Area Chart of Time Series')
plt.show()

# 20. Multivariate Time Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dates = pd.date_range('20210101', periods=50)
index = pd.date_range('2021-01-01', periods=120, freq='ME')

df.plot()
plt.title('Multivariate Time Series')
plt.show()

# 21. Seasonal Decomposition Plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
index = pd.date_range('20210101', periods=120, freq='M')
data = pd.Series(np.random.randn(120).cumsum(), index=index)
result = seasonal_decompose(data, model='additive', period=12)
result.plot()
plt.show()

# 22. Error Bars in Line Chart
import matplotlib.pyplot as plt
x = np.arange(10)
y = 2 * x + 1
errors = np.random.rand(10)
plt.errorbar(x, y, yerr=errors, fmt='-o')
plt.title('Line Chart with Error Bars')
plt.show()

# 23. Confidence Interval using Fill
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)
ci = 0.2
plt.plot(x, y)
plt.fill_between(x, y - ci, y + ci, color='b', alpha=0.2)
plt.title('Line Plot with Confidence Interval')
plt.show()

# 24. Categorical Bar Plot
import seaborn as sns
data = sns.load_dataset('tips')
sns.barplot(x='day', y='total_bill', data=data)
plt.title('Average Bill per Day')
plt.show()

# 25. Categorical Box Plot
sns.boxplot(x='day', y='total_bill', data=data)
plt.title('Box Plot of Bill per Day')
plt.show()

# 26. Categorical Violin Plot
sns.violinplot(x='day', y='total_bill', data=data)
plt.title('Violin Plot of Bill per Day')
plt.show()

# 27. Count Plot
sns.countplot(x='day', data=data)
plt.title('Count of Records per Day')
plt.show()

# 28. Swarm Plot
sns.swarmplot(x='day', y='total_bill', data=data)
plt.title('Swarm Plot of Bills per Day')
plt.show()

# 29. Strip Plot
sns.stripplot(x='day', y='total_bill', data=data)
plt.title('Strip Plot of Bills per Day')
plt.show()

# 30. Histogram with KDE Overlay
sns.histplot(data['total_bill'], kde=True)
plt.title('Histogram with KDE')
plt.show()

# 31. Scatter Plot with Hue
sns.scatterplot(x='total_bill', y='tip', hue='sex', data=data)
plt.title('Scatter Plot with Hue')
plt.show()

# 32. FacetGrid of Histograms
g = sns.FacetGrid(data, col='sex')
g.map(plt.hist, 'total_bill')
plt.show()

# 33. Line Plot by Category
sns.lineplot(x='size', y='total_bill', hue='sex', data=data)
plt.title('Line Plot by Category')
plt.show()

# 34. Boxen Plot
sns.boxenplot(x='day', y='total_bill', data=data)
plt.title('Boxen Plot')
plt.show()

# 35. Point Plot
sns.pointplot(x='day', y='total_bill', hue='sex', data=data)
plt.title('Point Plot')
plt.show()

# 36. Catplot with Kind='violin'
sns.catplot(x='day', y='total_bill', kind='violin', data=data)
plt.title('Catplot - Violin')
plt.show()

# 37. Relplot for Scatter
sns.relplot(x='total_bill', y='tip', data=data)
plt.title('Relplot - Scatter')
plt.show()

# 38. Relplot for Line
sns.relplot(x='size', y='tip', kind='line', data=data)
plt.title('Relplot - Line')
plt.show()

# 39. Jointplot with Kind='scatter'
sns.jointplot(x='total_bill', y='tip', data=data, kind='scatter')
plt.show()

# 40. Jointplot with Kind='hex'
sns.jointplot(x='total_bill', y='tip', data=data, kind='hex')
plt.show()

# 41. Jointplot with Kind='kde'
sns.jointplot(x='total_bill', y='tip', data=data, kind='kde')
plt.show()

# 42. Pairplot Colored
sns.pairplot(data, hue='sex')
plt.show()

# 43. Heatmap with Tips Correlation
tips_corr = data.corr(numeric_only=True)
sns.heatmap(tips_corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Tips Dataset')
plt.show()

# 44. Regression Plot
sns.regplot(x='total_bill', y='tip', data=data)
plt.title('Regression Plot')
plt.show()

# 45. Residual Plot
sns.residplot(x='total_bill', y='tip', data=data)
plt.title('Residual Plot')
plt.show()

# 46. Lmplot with Hue
sns.lmplot(x='total_bill', y='tip', hue='sex', data=data)
plt.title('LM Plot with Hue')
plt.show()

# 47. ECDF Plot
sns.ecdfplot(data['total_bill'])
plt.title('ECDF Plot')
plt.show()

# 48. Histogram of Size
sns.histplot(data['size'], bins=8, kde=False)
plt.title('Histogram of Size')
plt.show()

# 49. Barplot with Estimator
sns.barplot(x='day', y='tip', data=data, estimator=np.mean)
plt.title('Barplot of Mean Tip per Day')
plt.show()

# 50. Scatterplot with Size and Style
sns.scatterplot(x='total_bill', y='tip', size='size', style='sex', data=data)
plt.title('Scatterplot with Size and Style')
plt.show()

# 51. KDE Plot of Tip by Sex
sns.kdeplot(data=data, x='tip', hue='sex', fill=True)
plt.title('KDE Plot of Tip by Sex')
plt.show()


