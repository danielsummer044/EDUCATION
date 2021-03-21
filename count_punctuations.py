text = "Hello world! My name is - Daniel, im 19 year's old."
count = 0
punctuations = ('!',   ",",   ";",   "'",   ".",   "-",   "?")

for i in range(len(text)):
    if text[i] in punctuations:
        count = count + 1
print(count)