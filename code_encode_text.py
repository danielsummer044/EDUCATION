from string import ascii_lowercase, ascii_uppercase


def next_letter(letter):
	"""
	'A' -> 'B'
	'a' -> 'b'
	'Z' -> 'A'
	'z' -> 'a'
	"""
	coded_text = ''
	step = 1
	if letter in ascii_lowercase:
		coded_text = coded_text + ascii_lowercase[ascii_lowercase.index(letter) + step % len(ascii_lowercase)]

	if letter in ascii_uppercase:
		coded_text = coded_text + ascii_uppercase[ascii_uppercase.index(letter) + step % len(ascii_uppercase)]

	else:
		coded_text += text

	return coded_text

"""
def prev_letter(letter):

	if letter in ascii_uppercase:
		
	elif letter in ascii_lowercase:
		# get next letter
	return new_letter

"""
"""
def code(text):

	# TODO: make encoded_text
	for letter in text:
		next_letter(letter)
	return coded_text

"""
"""
def decode(text):

	return decoded_text
"""

# check
text = 'Hello world'
coded_text = ''

coded_text = next_letter(text)
print(coded_text)
"""
decoded_text = decode(text)
print(decoded_text)
"""