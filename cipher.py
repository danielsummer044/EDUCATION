from sting import ascii_lowercase, ascii_uppercase


def next_letter(letter):
	"""
	'A' -> 'B'
	'a' -> 'b'
	'Z' -> 'A'
	'z' -> 'a'
	"""
	if letter in ascii_uppercase:
		# get next letter
	elif letter in ascii_lowercase:
		# get next letter
	return new_letter


def prev_letter(letter):
	"""
	'B' -> 'A'
	'b' -> 'a'
	'A' -> 'Z'
	'a' -> 'z'
	"""
	if letter in ascii_uppercase:
		# get next letter
	elif letter in ascii_lowercase:
		# get next letter
	return new_letter


def encode(text):
	"""
	"Hello world" -> "Ifmmp xpsme"
	"""
	# TODO: make encoded_text
	for letter in text:
		next_letter(letter)
	return encoded_text


def decode(text):
	"""
	"Ifmmp xpsme" -> "Hello world" 
	"""
	return decoded_text


# check
text = 'Hello world'
encoded_text = encode(text)
print(encoded_text)
decoded_text = decode(text)
print(decoded_text)