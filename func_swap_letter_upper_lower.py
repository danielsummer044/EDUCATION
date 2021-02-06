"""
from string import ascii_lowercase, ascii_uppercase

text = 'Hello'
new_text = ''

for letter in text:
	if letter in ascii_lowercase:
		new_text = letter.upper()
	if letter in ascii_uppercase:
		new_text = letter.lower()
	print(new_text)
"""

from string import ascii_lowercase, ascii_uppercase

def upper_lower(letter):

	if letter in ascii_lowercase:
		new_text = letter.upper()
	if letter in ascii_uppercase:
		new_text = letter.lower()
	return new_text #???	D:

def reg(text):

	new_text = ''

	for letter in text:
		new_text += upper_lower(letter)
	return new_text

def main():

	text = 'heLLLLLLOOOooooOOOo'
	new_text = reg(text)
	print(new_text)

main()