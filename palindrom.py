words = ['abba', 'hello', 'sos', 'world']

def palindrom(word):
    """
    abba -> True
    hello -> False
    """
    new_word = ''
    for letter in word[::-1]:
        new_word += letter

    return new_word == word


def palindrom_2(word):
    # index = 0, len(word) - 1
    # index = 1, len(word) - 2
    # index = 2, len(word) - 3
    # index = len(word) - 1, 0

    flag = True
    for i in range(len(word)):
        last_i = len(word) - i - 1
        if word[i] != word[last_i]:
            flag = False
            break
    return flag



#print(palindrom('abba'))
#print(palindrom('hello'))

for word in words:
    print(palindrom_2(word))