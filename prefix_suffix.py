text = ['apple', 'hello', 'car', 'hell', 'argument', 'height', 'undo', 'prefire', 'unusual', 'prehistory', 'endorsement', 'anananaun', 'mentargu']

prefix = 'un'
suffix = 'ment'

prefix_len = len(prefix)
suffix_len = len(suffix)

for word in text:

    first = word[:prefix_len]
    last = word[-suffix_len:]

    if first == prefix or last == suffix:
        print(word)