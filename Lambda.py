add = lambda x, y: x + y
print(add(5, 3))


square = lambda x: x ** 2
print(square(4))


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


data = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)


multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))


numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


numbers = [10, 15, 20, 25, 30]
odds = list(filter(lambda x: x % 2 != 0, numbers))
print(odds)


students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

sorted_students = sorted(students, key=lambda student: student['score'])
print(sorted_students)


def make_multiplier(n):
    return lambda x: x * n


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))


check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(4))
print(check_even(7))


from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)


names = ["john", "DOE", "ALICE"]
capitalized = list(map(lambda name: name.capitalize(), names))
print(capitalized)


emails = ["alice@example.com", "bob@test.com"]
domains = list(map(lambda email: email.split('@')[1], emails))
print(domains)


numbers = [2, 4, 6, 8]

all_even = all(map(lambda x: x % 2 == 0, numbers))
print(all_even)

any_gt_5 = any(map(lambda x: x > 5, numbers))
print(any_gt_5)


words = ["apple", "banana", "cherry", "fig"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)


sentence = "lambda functions are powerful"
reversed_words = list(map(lambda word: word[::-1], sentence.split()))
print(" ".join(reversed_words))


people = ["Alice Johnson", "Bob Smith", "Charlie Brown"]
sorted_by_last = sorted(people, key=lambda name: name.split()[-1])
print(sorted_by_last)


operations = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mul': lambda x, y: x * y,
    'div': lambda x, y: x / y if y != 0 else 'Error'
}
print(operations['add'](10, 5))
print(operations['div'](10, 0))


numbers = list(range(1, 21))
filtered = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers))
print(filtered)


check_even_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check_even_odd(4))
print(check_even_odd(7))


s1 = 'GeeksforGeeks'

s2 = lambda func: func.upper()
print(s2(s1))


n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(5))
print(n(-3))
print(n(0))


li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())


check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(4))
print(check(7))


calc = lambda x, y: (x + y, x * y)

res = calc(3, 4)
print(res)


n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))


a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))


from functools import reduce

a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b)



