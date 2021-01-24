mas0 = [1001, 1010101, 10101110]

def remove_zero(number):
    """remove zeroes from number:
    1001 -> 11
    """
    s2 = ''
    s = str(number)
    for element in s:
        if element != "0":
            s2 = s2 + element
        
    return int(s2)


for number in mas0:
    print(remove_zero(number), end=', ')
