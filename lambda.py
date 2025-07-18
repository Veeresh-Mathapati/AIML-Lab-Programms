add=lambda x,y:x+y
print(add(5,3))

square=lambda x:x**2
print(square(4))

number=[1,2,3,4,5,6]
even_number=list(filter(lambda x:x%2==0,number))
print(even_number)

data=[(1,'apple'),(3,'banana'),(2,'cherry')]
sorted_data=sorted(data,key=lambda x:x[1])
print(sorted_data)

multiply=lambda x,y,z:x*y*z
print(multiply(1,2,3))

numbers=[1,2,3,4,5]
double=list[map(lambda x:x*2,numbers)]
print(double)

number=[10,15,20,25,30]
odds=list(filter(lambda x:x%2!=0,number))
print(odds)

student=[
    {"name":"alice","score":85},
    {"name":"bob","score":92},
    {"name":"charile","score":78}
]
sorted_student=sorted(student,key=lambda student:student['score'])
print(sorted_student)
