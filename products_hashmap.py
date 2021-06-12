products = {'Onion': 23.75, 'Fish': 45.00, 'Oil': 62.25, 'Bread': 24.50, 'Milk': 35.00 }
money = 500

name = []
for key,value in products.items():
    name.append(key)

price = []
for key, value in products.items():
    price.append(value)

# how much can you buy
def count(price, money):
    for i in range(len(price)):
        x = money // price[i]
        print(int(x), name[i])
        print('-' * 10)
    return None

# how much maximum products you can buy
def maximum(price, money):
    maximum = 0
    for i in range(len(price)):
            x = money // price[i]
            x = int(x)
            if x > maximum:
                maximum = x
    print("Maximum products you can buy:", maximum)
    return None

print(count(price, money))
print(maximum(price, money))