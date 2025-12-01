def total_cost(price, Quantity):
    cost = price * Quantity
    return cost



price = int(input("Enter the price: "))
quantity = int(input('Enter the Quantity: '))

pay = total_cost(price, quantity)
print(f'Please Pay: {pay}')