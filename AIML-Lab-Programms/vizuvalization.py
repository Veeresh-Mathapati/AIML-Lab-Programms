import pandas as pd
iris = pd.read_csv('docs.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
iris.tail()
iris.describe()

import matplotlib.pyplot as plt
x=iris['petal_length']
y=iris['petal_width']
plt.scatter(x,y)
plt.title("Scatter plot Petal length vs width")
plt.xlabel("petal length")
plt.ylabel("Petal width")
plt.show()

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
# scatter the sepal_length against the sepal_width
ax.scatter(iris['sepal_length'], iris['sepal_width'])
# set a title and labels
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')
plt.show()

colors = {'Iris-setosa':'r', 'Iris-versicolor':'g', 'Iris-virginica':'b'}
species_colors = iris['class'].map(colors)
fig, ax = plt.subplots()
ax.scatter(iris['sepal_length'],iris['sepal_width'],c=species_colors)
ax.set_title("Scatter Plot of Iris Dataset")
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal width')

"""How many flowers belong to each species?"""

species_counts = iris['class'].value_counts()

plt.bar(species_counts.index, species_counts.values, color='lightblue')
plt.title("Number of Flowers by Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.grid(axis='y')

"""What is the distribution of petal length?"""

plt.hist(iris['petal_length'], bins=10, color='lightgreen', edgecolor='black')
plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.grid(True)


