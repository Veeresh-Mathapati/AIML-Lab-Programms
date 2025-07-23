import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])
print("Array a:", a)
print("Array b:", b)
print("Sum:", a + b)
print("Difference:", b - a)
print("Product:", a * b)
print("Mean of a:", np.mean(a))
print("Max of b:", np.max(b))
print("Min of b:", np.min(b))


arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Element at (0, 1):", arr[0, 1])
print("Second row:", arr[1])
print(arr)


a = np.array([5, 10, 15])
b = np.array([1, 2, 3])
print("Sum:", a + b)


rand_array = np.random.randint(1, 100, size=10)
print("Random Array:", rand_array)
print("Maximum:", np.max(rand_array))
print("Minimum:", np.min(rand_array))


arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)
print("Reshaped (2x3):\n", reshaped)
flattened = reshaped.flatten()
print("Flattened:", flattened)


arr = np.array([10, 20, 30, 40, 50])
filtered = arr[arr > 25]
print("Elements > 25:", filtered)


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.dot(A, B)
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("A x B:\n", result)


data = np.array([1, 2, 3, 4, 5, 6])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))


a = np.arange(0, 10)
b = np.linspace(0, 2 * np.pi, 10)
print("Arange:", a)
print("Linspace:", b)


matrix = np.array([[1, 2, 3], [4, 5, 6]])
transpose = matrix.T
print("Original:\n", matrix)
print("Transposed:\n", transpose)


import numpy as np
x = np.array([0, np.pi/2, np.pi])
# Apply sine function
y = np.sin(x)
print("x values:", x)
print("sin(x):", y)


import pandas as pd
data1 = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'Score': [85, 90, 95]
}
df1 = pd.DataFrame(data1)
print(df1)


# Assuming 'students.csv' exists
# df2 = pd.read_csv("students.csv")
# print(df2.head())
# print(df2.info())
# print(df2.describe())


data2 = {
    'Name': ['Asha', 'Ravi', 'Neha'],
    'Age': [24, 29, 26]
}
df2 = pd.DataFrame(data2)
filtered_df = df2[df2['Age'] > 25]
print(filtered_df)


data3 = {
    'Department': ['CS', 'CS', 'IT', 'IT'],
    'Marks': [85, 90, 78, 82]
}
df3 = pd.DataFrame(data3)
grouped = df3.groupby('Department').mean()
print(grouped)


import pandas as pd

data = {
    'Math': [90, 80, 85],
    'Science': [95, 75, 88]
}
df = pd.DataFrame(data)
df['Average'] = (df['Math'] + df['Science']) / 2
print(df)
df.to_csv("averages.csv", index=False)


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 12, 15, 18, 20]

plt.plot(x, y)
plt.title("Simple Line Graph")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()


import matplotlib.pyplot as plt

students = ['Asha', 'Ravi', 'Neha']
scores = [85, 90, 78]

plt.bar(students, scores, color='skyblue')
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()


import matplotlib.pyplot as plt

labels = ['Python', 'Java', 'C++', 'C']
sizes = [40, 25, 20, 15]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Programming Language Usage")
plt.axis('equal')
plt.show()


import matplotlib.pyplot as plt

ages = [18, 22, 21, 25, 30, 30, 27, 25, 22, 19]

plt.hist(ages, bins=5, color='green')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 7, 6, 8, 10]

plt.scatter(x, y, color='red')
plt.title("Scatter Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()



