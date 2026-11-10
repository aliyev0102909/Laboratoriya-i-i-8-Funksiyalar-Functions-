def calculate_total(prices, discount=0):
    total = sum(prices)
    return total - total * discount / 100
def describe_order(customer, city, country="Azerbaijan"):
    return customer + " ordered from " + city + ", " + country
order_total = calculate_total([10, 20, 30], 10)
print("Total: " + str(order_total))
print(describe_order(customer="Ali", city="Baku"))
