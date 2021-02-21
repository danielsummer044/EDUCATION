from pass_2 import get_new_letter, encode, to_int
from string import ascii_lowercase, ascii_uppercase


def test_get_new_letter():
    """
    'abc....xyz', 'a', step = 1, => b
    """

    assert get_new_letter(ascii_lowercase, 'a', 1) == 'b'
    assert get_new_letter(ascii_lowercase, 'z', 1) == 'a'
    assert get_new_letter(ascii_lowercase, 'a', -1) == 'z'

    assert get_new_letter(ascii_uppercase, 'A', 1) == 'B'
    assert get_new_letter(ascii_uppercase, 'Z', 1) == 'A'
    assert get_new_letter(ascii_uppercase, 'A', -1) == 'Z'

    print('test passed')


def test_get_new_letter_step():

    assert get_new_letter(ascii_lowercase, 'd', -3) == 'a'
    assert get_new_letter(ascii_lowercase, 'a', 3) == 'd'

    assert get_new_letter(ascii_uppercase, 'D', -3) == 'A'
    assert get_new_letter(ascii_uppercase, 'A', 3) == 'D'

    print('test passed')

def test_encode():

    assert encode('Hello', '1') == 'Ifmmp'
    print('test passed')


def test_to_int():
    assert to_int('a') == 0
    assert to_int('b') == 1
    assert to_int('5') == 5
    print('test passed')


test_get_new_letter()
test_get_new_letter_step()
test_encode()
test_to_int()