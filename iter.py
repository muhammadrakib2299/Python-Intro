numbers = [10, 45, 65, 23, 89, 78, 11]
numbers_iter = iter(numbers)

# print(next(numbers_iter))
# print(next(numbers_iter))
# print(next(numbers_iter))
# print('I am trying to learn iterator')
# print(next(numbers_iter))
# print(next(numbers_iter))

try:
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print('I am trying to learn iterator')
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
except StopIteration:
    print('Iteration is stopped')