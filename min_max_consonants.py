text = ['School', 'apple', 'Car', 'onion', 'We', 'wood', 'Smile']
#			4		3		2		2		1		2		3
consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'


max_consonants = 0 # ?1
min_consonants = 0

max_word = ''
min_word = ''

for word in text:

# ?2
	amount_of_consonants_in_word = 0

	for letter in word:

		if letter in consonants:
			amount_of_consonants_in_word += 1

	if amount_of_consonants_in_word > max_consonants:
		max_consonants = amount_of_consonants_in_word
#		max_word = word

		print(max_consonants, word)
