import numpy as np
A = np.array([1,2,3,4,5])
B= np.array([10,20,30,40,50])

sum_array=A+B
diff_array=A-B
product_array=A*B

mean_a=np.mean(A)
max_B=np.max(B)
min_B=np.min(B)

print("Array A:",A)
print("Array B:",B)
print("sum:",sum_array)
print("Differenece:",diff_array)
print("Product:",product_array)
print("Mean of A:",mean_a)
print("Max of B:",max_B)
print("Min of B:",min_B)

arr=np.array([[1,2,3],[4,5,6,]])
print("Element at(0,1)",arr[0,1])
print("Second row",arr[1])
print(arr)


a=np.array([5,10,15])
b=np.array([1,2,3])
result=a+b
print("Sum",result)

rand_array=np.random.randint(1,200,size=10)
print("Random Array",rand_array)
print("Maximum",np.max(rand_array))
print("Minimum",np.min(rand_array))

arra=np.array([6,3,2,4,5,1])
reshaped=arra.reshape(2,3)
print("Reshaped(2*3:\n",reshaped)
flattend=reshaped.flatten()
print("Flattend",flattend)


import numpy as nr
arry=nr.array([10,20,30,40,50])
filteres=arr[arr>25]
print("Elemrnt>25",filteres)

import numpy as nm
c=nm.array([[1,2],[3,4]])
d=nm.array([[5,6],[7,8]])

result=nm.dot(c,d)
print("Matrix C:/n",c)
print("Matrix D:/n",d)
print("C*D:/n",result)

data=np.array([1,2,3,4,5,6])
print("mean:",np.mean(data))
print("median:",np.median(data))
print("standard Deviation",np.std(data))

import numpy as bv
ab=bv.arange(0,10)
cd=bv.linspace(0,2*bv.pi,10)
print("Arrange:",ab)
print("Linespace:",cd)

matrix=bv.arange(0,20)
transper=matrix.T
print("Original",matrix)
print("Transposed",transper)

m=np.array([0,np.pi/2,np.pi])
t=np.sin(m)
print("m value:",m)
print("t value:",t)

import pandas as pd
datas={
    'Name':['Alice','bob','charlie'],
    'Age':[25,30,22],
    'Score':[85,90,95]
}
df=pd.DataFrame(datas)
print(df)

filtered_df=df[df['Age']<25]
print(filtered_df)

data1={
    'Department':['CS','IC','EE','IT'],
    'Marks':[85,90,78,82],
}
df=pd.DataFrame(data1)
grouped=df.groupby('Department').mean()
print(grouped)

import pandas as dp
data2={
'maths':[90,54,78,96],
'Science':[95,74,61,36]
}

df=dp.DataFrame(data2)
df['Average'] = (df['maths'] + df['Science']) / 2
print(df)
df.to_csv("average.csv", index=False)

#lineGraph

import matplotlib.pyplot as plt
xm=[1,2,3,4,5]
ym=[10,20,18,10,20]

plt.plot(xm,ym)
plt.title("Simple Line Graph")
plt.xlabel("XM Values")
plt.ylabel("YM Values")
plt.show()

students=['Asha','Ravi','Neha']
scores=[85,90,78]
plt.bar(students,scores,color='Skyblue')
plt.title("Student Score")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

