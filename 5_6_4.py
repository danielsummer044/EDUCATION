array = [30, 25, 5, -36, 100, 255]
for n in range(len(array)):
    if array[n] > 0 and array[n] % 5 == 0 and array[n] % 6 == 0 and array[n] % 4 != 0:
        print(array[n])