def isPalindrom(n):
    result = str(n)
    return result == result[::-1]
    


userInput = int(input('Enter you number: '))
output = isPalindrom(userInput)
print(output)