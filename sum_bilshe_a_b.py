arr = [21, 23, 31, 34, 11, 111, 17, 12, 7, 5]

a = 2
b = 6
summ = 0

def find_sum(n):
    summ = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        summ += digit
    return summ

for i in range(len(arr)):
    summ = find_sum(arr[i])

    if summ > a and summ < b:
        print(arr[i])