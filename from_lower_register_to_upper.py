words = "Hello, my name is Daniel"
#word = words.split()

letters = list(words)
for i in range(len(letters)):	#for letter in words:
	if letters[i] == "o":
		letters[i] = "O"
		print(letters)