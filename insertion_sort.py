array = [8, 7, 21, 54, 1, 56, 47, 421, 321]

def sort(number):
    for i in range(len(array)):
        first = array[i]
        j = i - 1
        while j >= 0 and array[j] < first:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = first

sort(array)
print(array)