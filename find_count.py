arr = [21, 23, 31, 34, 11, 111, 17, 12, 7, 5]
a = 2
b = 4
def find_count(n):
    count = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        count = count + 1
    return count

for i in range(len(arr)):
    count = find_count(arr[i])
    if count > a and count < b:
        print((arr[i]))
