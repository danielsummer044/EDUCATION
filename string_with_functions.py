from string import ascii_lowercase, ascii_uppercase

def punctuation_counter(string):
    count = 0
    for element in string:
        if element in punctuation_marks:
            count = count + 1
    return count
"""
def lower_upper_case(string):
    new_string = ""
    for letter in string:
        if letter in ascii_uppercase:
            new_string = string.replace(letter, letter.lower())
        if letter in ascii_lowercase:
            new_string = string.replace(letter, letter.upper())
    return new_string
"""
def punctuation_remover(string):
    for element in string:
       if element in punctuation_marks:
           string = string.replace(element, "")
    return string

def reverse(string):
    return string[::-1]

punctuation_marks = (".", ",", ":", ";", "?", "!", "-", "`", "'")
string = "Daniel: - 'Hello! Today is a good spring day. Isn`t it?'"

print("Punctuation marks:", punctuation_counter(string))
print("Reverse:", reverse(string))
print("Remove:", punctuation_remover(string))
print(lower_upper_case(string))