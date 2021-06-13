products = {'Onion': 23.75, 'Fish': 45.00, 'Oil': 62.25, 'Bread': 24.50, 'Milk': 35.00 }
money = 500

# how much can you buy
def count(price, money):
    x = money // price
    return int(x)

# product -> key, price -> value
iteration = 0
for key, value in products.items():
    if iteration == 0:
        maximum = count(value, money)
        max_product = key
    else:
        if count(value, money) > maximum:
            maximum = count(value, money)
            max_product = key
    iteration += 1

print(maximum, max_product)