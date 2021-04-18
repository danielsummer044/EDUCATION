# N = 15 => 1,2,3....15
# print numbers % 3 - > Fizz, % 5 -> Buzz, % 3 % 5 -> FizzBuzz

n = 30
for i in range(1, n+1):
    if (i % 3 == 0 and i % 5 == 0) or (i % 4 == 0 and i % 7 == 0):
        print(i, 'FizzBuzz')

    elif i % 3 == 0 or i % 4 == 0:
        print(i, 'Fizz')

    elif i % 5 == 0 or i % 7 == 0:
        print(i, 'Buzz')

    else:
        print(i)