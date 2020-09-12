words = ["apple", "onions", "cucumber", "tree", "hi"]

lowest_word = words[0]
largest_word = words[0]

for word in range(1, len(words)):
	if lowest_word < words[word]:
		lowest_word = words[word]

print(lowest_word)