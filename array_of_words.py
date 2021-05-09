letters = [['a', 't', 'z'],
           ['c', 'o', 'w'],
           ['a', 'r', 'c']]

words = ['arc', 'cow', 'the']

for row in letters:
    slovo = ''.join(row)
    print(slovo)
    """
    slovo = ''
    for letter in row:
        slovo += letter
    print(slovo)
    """