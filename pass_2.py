from string import ascii_lowercase, ascii_uppercase

text = 'hello'

password = 2413
pass_digits = []

while password > 0:
	pass_digits.insert(0, password % 10)
	password = (password - password % 10) // 10
print(pass_digits)


for digits in pass_digits:
	print(digits)

#indexes_of_letters
for letter in text:
	if letter in ascii_lowercase:
		indexes_of_letters = ascii_lowercase.index(letter)
		print(indexes_of_letters)



def get_pass_digits(password):

	pass_digits = []

	while password > 0:
		pass_digits.insert(0, password % 10)
		password = (password - password % 10) // 10
	return pass_digits



def get_index_of_letters(text):

	for letter in text:
		if letter in ascii_lowercase:
			indexes_of_letters = ascii_lowercase.index(letter)
	return indexes_of_letters



def get_new_letter(letter):

	new_letter_index = get_pass_digits(password) + get_index_of_letters(text)
	new_letter = new_letter_index
	return new_letter

print(get_new_letter('h'))

