import pandas as pd

# From a list
s1 = pd.Series([10, 20, 30, 40])
print(s1)

# With custom index
s2 = pd.Series([1.5, 2.5, 3.5], index=['a', 'b', 'c'])
print(s2)

# From a dictionary
s3 = pd.Series({'math': 85, 'science': 90, 'english': 78})
print(s3)


import pandas as pd

ds1 = pd.Series([2, 4, 8, 10])
ds2 = pd.Series([1, 3, 7, 9])

print("Multiply two Series:")
ds = ds1 * ds2
print(ds)

print("Divide Series1 by Series2:")
ds = ds1 / ds2
print(ds)


import pandas as pd

d1 = {'a': 100, 'b': 200, 'c': 300}
print("Original dictionary:")
print(d1)

new_series = pd.Series(d1)
print("Converted series:")
print(new_series)


import pandas as pd

s = pd.Series([400, 300.12, 100, 200])
print("Original Data Series:")
print(s)

new_s = s.sort_values()
print(new_s)


import pandas as pd

s = pd.Series(data=[1, 2, 3], index=['A', 'B', 'C'])
print("Original Data Series:")
print(s)

s = s.reindex(index=['B', 'A', 'C'])
print("Data Series after changing the order of index:")
print(s)


import pandas as pd
import numpy as np

sr1 = pd.Series([1, 2, 3])
sr2 = pd.Series([2, 3, 6])

print("Original Series:")
print("sr1:")
print(sr1)
print("sr2:")
print(sr2)

print("\nItems of a given series not present in another given series:")
sr11 = pd.Series(np.union1d(sr1, sr2))
sr22 = pd.Series(np.intersect1d(sr1, sr2))
result = sr11[~sr11.isin(sr22)]
print(result)


import pandas as pd

exam_data = {'name': ['Manish', 'Dhiraj'], 'score': [12.5, 9]}
labels = ['NAME', 'SCORE']

df = pd.DataFrame(exam_data, index=labels)
print(df)


import pandas as pd

exam_data = {'name': ['Manish', 'Dhiraj', 'Man', 'Dhir'], 'score': [12.5, 91, 2.5, 9]}
df = pd.DataFrame(exam_data)

print("First three rows of the data frame:")
print(df.iloc[:3])  # OR df.head(3)


import pandas as pd

exam_data = {'name': ['Manish', 'Dhiraj', 'Man', 'Dhir'], 'score': [12.5, 91, 2.5, 9]}
df = pd.DataFrame(exam_data)

total_rows = len(df.axes[0])
total_cols = len(df.axes[1])
print("Number of Rows: " + str(total_rows))
print("Number of Columns: " + str(total_cols))


import pandas as pd

exam_data = {'name': ['Manish', 'Dhiraj', 'Man', 'Dhir'], 'score': [12.5, 91, 20.5, 19]}
df = pd.DataFrame(exam_data)

print("Rows where score between 15 and 20 (inclusive):")
print(df[df['score'].between(15, 20)])


import pandas as pd

exam_data = {'name': ['Manish', 'Dhiraj', 'Man', 'Dhir'], 'score': [12.5, 91, 20.5, 19]}
df = pd.DataFrame(exam_data)

result_sort = df.sort_values(by=['name', 'score'], ascending=[False, True])
print("Sort the data frame first by 'name' in descending order, then by 'score' in ascending order:")
print(result_sort)


import pandas as pd

exam_data = {'name': ['Manish', 'Dhiraj', 'Man', 'Dhir'], 'score': [12.5, 91, 20.5, 19]}
df = pd.DataFrame(exam_data)

df['name'] = df['name'].replace('Manish', 'Anish')
print(df)


import pandas as pd

exam_data = {'name': ['Manish', 'Dhiraj', 'Man', 'Dhir'], 'score': [12.5, 91, 20.5, 19]}
df = pd.DataFrame(exam_data)

medium = ['english', 'hindi', 'hindi', 'english']
df['medium'] = medium

print("\nNew DataFrame after inserting the 'medium' column")
print(df)


import pandas as pd

exam_data = {'name': ['Manish', 'Dhiraj', 'Man', 'Dhir'], 'score': [12.5, 91, 20.5, 19]}
df = pd.DataFrame(exam_data)

df = df.rename(columns={'name': 'NAME', 'score': 'SCORE'})
print("New DataFrame after renaming columns:")
print(df)


import pandas as pd

exam_data = {'name': ['Manish', 'Dhiraj', 'Man', 'Dhir'], 'score': [12.5, 91, 20.5, 19]}
df = pd.DataFrame(exam_data)

df = df[df.score >= 20]
print("New DataFrame")
print(df)


import pandas as pd

s1 = pd.Series(['100', '200', '400'])
s2 = pd.Series(['10', '20', '40'])

print("Data Series:")
print(s1)
print(s2)

df = pd.concat([s1, s2], axis=1)
print("New DataFrame combining two series:")
print(df)


import pandas as pd

s1 = pd.Series(['100', '200', '400'])
s2 = pd.Series(['10', '20', '40'])
df = pd.concat([s1, s2], axis=1)

print("Value of Row 4:")
print(df.iloc[2])


import pandas as pd

s1 = pd.Series(['100', '200', '400'])
s2 = pd.Series(['10', '20', '40'])
df = pd.concat([s1, s2], axis=1)

new_col = [1, 2, 3]
idx = 0  # Insert at position 0
df.insert(loc=idx, column='1', value=new_col)

print("\nNew DataFrame after inserting column at position 0:")
print(df)





