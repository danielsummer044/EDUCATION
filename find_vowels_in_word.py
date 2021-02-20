vowels = 'AEIOUYaeiouy'
#vowels = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']

text = ['Hello', 'my', 'NAME', 'is', 'Daniel']
#		  2	      1	     2		1		3
amount_of_voewls_in_text = 0

for words in text:
	for letters in words:
		if letters in vowels:
			amount_of_voewls_in_text += 1
	if letters != vowels:
		break

print(amount_of_voewls_in_text)