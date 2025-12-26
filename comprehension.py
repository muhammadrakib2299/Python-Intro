numebrs = [12, 14, 45, 65, 18, 20, 22, 23, 89, 78, 11, 13, 25, 28, 30, 31]

# odd_numbers = []
# for num in numebrs:
#     if num%2 == 1:
#         odd_numbers.append(num)

# print('All numbers : ', numebrs)
# print('Odd Numbers : ', odd_numbers)

evenumbers = [num for num in numebrs if num%2 == 0]
print(evenumbers)