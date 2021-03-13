text = ['apple', 'hello', 'car', 'hell', 'argument', 'height', 'undo', 'prehistory', 'endorsement', 'anananaun']

text_2 = []
index = 0

for word_1 in text:
    for word_2 in text[index:]:

        if word_1 != word_2:
            w_1_f = word_1[:2]
            w_2_f = word_2[:2]

            if w_1_f == w_2_f:
                string = word_1 + " = " + word_2
                if text_2.count(string) == 0:
                    text_2.append(string)
    index = index + 1

print(text_2)