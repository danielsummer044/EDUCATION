vowels = 'AEIOUYaeiouy'
#vowels = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']

text = ['Hello', 'my', 'NAME', 'is', 'Daniel']
#		  2	      1	     2		1		3

slovo_max_golosni = ''
max_golosni = 0

for word in text:
	amount_of_voewls_in_word = 0
	for letters in word:
		if letters in vowels:
			amount_of_voewls_in_word += 1

	if amount_of_voewls_in_word > max_golosni:
		max_golosni = amount_of_voewls_in_word
		slovo_max_golosni = word

print(slovo_max_golosni)

