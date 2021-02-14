words = ['Hello', 'World', 'slovo']
golosni = ['a', 'e', 'i', 'o', 'u']
# result: e, o, o

def print_golosni(word):
    for letter in golosni:
        for letter_w in word:
            if letter == letter_w:
                print(letter)

for word in words:
    print_golosni(word)

