# def square(x):
#     return x*x
# result = square(5)
# print(result)

# multiply 
# square = lambda x: x*x 
# result = square(8)
# print(result)

# add two numbers
# add = lambda x, y: x + y
# sum = add(10, 5)
# print(sum)


numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 25]

# double_it = lambda x: x*x

# numbers_double = map(double_it, numbers)
# print(numbers)
# print(list(numbers_double))

# findbigs = filter(lambda num: num > 9, numbers)
# print(numbers)
# print(list(findbigs))


users = [
    {'name': 'Sakil', 'age': 50, },
    {'name': 'rakib', 'age': 30, },
    {'name': 'rony', 'age': 17, },
    {'name': 'khalid', 'age': 26, },
    {'name': 'tanvir', 'age': 29, },
    ]

senior_member = filter( lambda member: member['age'] > 29, users)
# print(users)
print('Senior Member: ',list(senior_member))