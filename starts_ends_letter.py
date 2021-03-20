text = ['apple', 'dad', 'tree', 'hello', 'mom', 'brother', 'sisters']

for word in text:
    for letter in word:
        if word.startswith(letter) and word.endswith(letter):
            print(word)    


"""
for word in text:
    for letter in word:

        len_of_word = len(word)
        first_letter = word[0]
        last_letter = len_of_word - 1

        if first_letter == word[last_letter]:
            print(word)
"""