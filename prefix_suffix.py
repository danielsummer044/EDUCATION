text = ['apple', 'hello', 'car', 'hell', 'argument', 'height', 'undo', 'prefire', 'unusual', 'prehistory', 'endorsement', 'anananaun', 'mentargu']

prefix = 'un'
suffix = 'ment'

for word in text:

    if word.startswith(prefix):
        print(word)

    if word.endswith(suffix):
        print(word)