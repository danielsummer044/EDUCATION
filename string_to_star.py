string = "qwerty zxc nkop kiolpujyhtg tyu qwertyui zs"

words = string.split()

min_word = words[0]
max_word = words[0]

min_index = 0
max_index = 0

for i in range(1, len(words)):
	if len(min_word) > len(words[i]):
		min_word = words[i]
		min_index = i

for i in range(1, len(words)):
	if len(max_word) < len(words[i]):
		max_word = words[i]
		max_index = i

if max_index > min_index:
	for i in range(min_index+1, max_index):
		words[i] = "*" * len(words[i])

if max_index < min_index:
	for i in range(max_index+1, min_index):
		words[i] = "*" * len(words[i])


string = ' '.join(words)



print(string)
