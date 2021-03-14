text = ['apple', 'hello', 'car', 'hell', 'argument', 'height', 'undo', 'prehistory', 'endorsement', 'anananaun', 'cap']

text_2 = []
index = 0
added_words = []


for word_1 in text:
    group = []
    for word_2 in text[index:]:

        if word_1 != word_2:
            w_1_f = word_1[:2]
            w_2_f = word_2[:2]
            if w_1_f == w_2_f:
                if word_1 not in added_words:
                    group.append(word_1)
                    added_words.append(word_1)
                if word_2 not in added_words:
                    group.append(word_2)
                    added_words.append(word_2)

    # if group is not empty
    # if len(group) > 0:
    if group:
        text_2.append(group)
    index = index + 1

print(text_2)