# largest = max(45, 89, 31, 112, 20, 280)
# nums = {12, 15, 50, 70, 90, 14}
# big_num = max(nums)

# print(largest)
# print(big_num)


# reversed
# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# number_revers = reversed(nums)
# print('Revers Number: ', list(number_revers))


# sorted numbers
# nums = [200, 12, 15, 50, 70, 90, 14, 150]
# shorted_numbers = sorted(nums, reverse=True)
# print(shorted_numbers)

actors = [
    {'name': 'Sakib', 'age': 35},
    {'name': 'salman khan', 'age': 65},
    {'name': 'sharukh khan', 'age': 61},
    {'name': 'salman sah', 'age': 27},
    {'name': 'aiub baccu', 'age': 40},
]


sorted_actor = sorted(actors, key=lambda actor: actor['age'], reverse=True)
print(sorted_actor)