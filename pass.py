from string import ascii_lowercase, ascii_uppercase

# abcdefghijklmnopqrstuvwxyz	jimoq

text = 'hello'
new_text = ''

password = 2413
pass_digits = []

#

while password > 0:
	pass_digits.insert(0, password % 10)
	password = (password - password % 10) // 10
#print(pass_digits)

"""
for letter in text:
	if letter in ascii_lowercase:
		new_text = text[0] + pass_digits[0]
print(new_text)
"""

txt_letter_index = ascii_lowercase.index('h')
print(txt_letter_index)

element = pass_digits[0]
print(element)

print()

# print new letter
new_index = txt_letter_index + element
new_letter = ascii_lowercase[new_index]
print(new_letter)

# elements of password

for digit in range(len(pass_digits)):
	print(pass_digits[digit])

# text indexes in ascii
for letter in text:
	txt_indexes = []
	if letter in ascii_lowercase:
		new_letter = ascii_lowercase.index(letter)
		print(new_letter)


"""
def new_letter(letter):

	new_index = ascii_lowercase.index(letter) + pass_digits[digit]
	if new_index > len(ascii_lowercase) - 1:
		new_letter = ascii_lowercase[new_index]
	return new_letter
"""
#new_index =  + pass_digits[digit]
"""

if letter in ascii_lowercase:
	new_text = new_text +
"""