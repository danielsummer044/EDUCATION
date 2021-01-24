mas = [7, 3, 0, 9, 4, 11, 31, 8]

for i in range(len(mas)):
    if i > 0 and i < len(mas) - 1:
       if mas[i] < mas[i-1] and mas[i] < mas[i+1]:
            print(mas[i])
