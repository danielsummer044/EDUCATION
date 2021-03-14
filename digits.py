# n = 123  , kilkist = 3, suma = 6
n = 1234

def find_sum(n):
    summ = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        summ += digit
    return summ


def find_count(n):
    count = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        count = count + 1
    return count


print(find_sum(n))
print(find_count(n))