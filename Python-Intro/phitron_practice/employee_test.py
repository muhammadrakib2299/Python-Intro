def show_employe(name, salary):
    print('Name:', name)
    print('Salary:', salary)


eName = input('Enter Name: ')
esalary = input('Enter Salary: ')

if eName == "":
    eName = 'Anonymous'


if esalary == "":
    esalary = 9000
else:
    esalary = int(esalary)

show_employe(eName, esalary)
