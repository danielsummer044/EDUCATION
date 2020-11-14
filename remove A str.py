string = "qwerty bjo adgjl fome anyr rekan aodo"

words = string.split(" ")

result = [i for i in string.split() if not i.startswith('a')]

print(result)