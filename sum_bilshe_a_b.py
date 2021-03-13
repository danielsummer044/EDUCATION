arr = [21, 23, 31, 34, 11, 17, 12, 7, 5]

a = 2
b = 6
summ = 0

def find_sum(number):

    digit = arr[i] % 10
    arr[i] = arr[i] // 10
    summ = digit + arr[i]
    return summ

for i in range(len(arr)):
    summ = find_sum(arr)

    if summ > a or summ < b:
        print(summ)