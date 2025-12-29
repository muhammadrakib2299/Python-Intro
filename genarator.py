numbers = [10, 20, 30, 45, 65, 78, 90, 97, 60]

def getNumbers (nums):
    for num in nums:
        yield num


result = getNumbers(numbers)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print('learn to generator')
print(next(result))
print(next(result))
print(next(result))
print(next(result))
