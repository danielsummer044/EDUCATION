products = ['Onion', 'Fish', 'Oil', 'Bread', 'Milk']
price = [23.75, 45.00, 62.25, 24.50, 35.00]
#        onion  fish    oil   bread   milk

money = 500

# how much can you buy
def count(price, money):
    for i in range(len(price)):
        x = money // price[i]
        print(int(x), products[i])
    return None#???

print(count(price, money))

print('---' * 10)

# how much maximum products you can buy
def maximum(price, money):
    maximum = 0
    for i in range(len(price)):
            x = money // price[i]
            x = int(x)
            if x > maximum:
                maximum = x
    print(maximum)#PRODUCT??? - ONION
    return None

print(maximum(price, money))
