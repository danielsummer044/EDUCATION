arr = [101, 12, 10, 222, 11, 100, 1]

def find_summ(number):
    summ = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        summ += digit
    return summ

def find_count(number):
    count = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        count = count + 1
    return count

for i in range(len(arr)):
    summ = find_summ((arr[i]))
    count = find_count((arr[i]))
    if count > summ:
        print(arr[i])