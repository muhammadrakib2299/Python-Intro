# with open ('massage.txt', 'w') as filewrite:
#     filewrite.write('Hello from python, i am new learn')

with open ('massage.txt', 'r') as fileRead:
    text = fileRead.read()

print(text)