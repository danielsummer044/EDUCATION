from string import ascii_lowercase, ascii_uppercase

text = 'dkghokdghopAAAAAAAfghgfbnvbnretwwquouipiuopAAAAdkhotkyr0k59-kk53gki53g53k5klk%^%^%_&)%_+)_+)$_+)%^$%$)(^+_)%(&_('
new_text = ''

for elem in text:
	if elem in ascii_lowercase:
		new_text += str(elem)
	if elem in ascii_uppercase:
		new_text += str(elem)
print(new_text)