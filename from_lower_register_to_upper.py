words = "Hello, my name is Daniel"


def golosni_upper(string):
    golosni = 'aeiou'

    s2 = ''

    for symbol in string:
        if symbol in golosni:
            s2 = s2 + symbol.upper()
        else:
            s2 += symbol
    return s2

print((golosni_upper(words)))
print((golosni_upper('a x e i x o x u')))
