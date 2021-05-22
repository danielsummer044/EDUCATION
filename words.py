letters = [['a', 't', 'z'],
           ['c', 'o', 'w'],
           ['a', 'r', 'c']]

words = ['aca', 'cow', 'tor']

for j in range(0, len(letters)):
    l_word = ''
    for i in range(0, len(letters[j])):
        l_word += letters[i][j]
    for w in range(0, len(words)):
        if l_word == words[w]:
            print(words[w])