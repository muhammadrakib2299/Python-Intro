def calcu(num1, num2):
    sum = num1 + num2
    
    if num1 > num2:
        sub = num1 - num2
    else:
        sub = num2 - num1

    return sum, sub


result = calcu(10, 10)
print(result)
