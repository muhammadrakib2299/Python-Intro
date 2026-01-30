# numbers = [12, 45, 23, 64, 78, 11, 10]
# # total = sum(numbers)
# # print(total)
# total = 0
# for i in numbers:
#     total = total + i
#     # print(total)
# print('after Sum: ', total)


# nums = {10, 12, 14, 16, 18, 24, 28, 32, 34, 38}
# total = 0

# for num in nums:
#     total += num

# print('Total :', total)


# Dectionary 
marks = {'bangla': 33, 'english': 44, 'math': 56, 'physic': 64, 'chemistry': 74, 'islam': 89}

# for mark in marks:
#     value = marks[mark]
#     print(mark, value)

for subject, mark in marks.items():
    print(subject, mark)