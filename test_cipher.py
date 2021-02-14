from cipher import get_new_letter
from string import ascii_lowercase, ascii_uppercase


def test_get_new_letter():
    """
    'abc....xyz', 'a', step = 1, => b
    """
    assert get_new_letter(ascii_lowercase, 'a', 1) == 'b'
    assert get_new_letter(ascii_lowercase, 'z', 1) == 'a'
    assert get_new_letter(ascii_lowercase, 'a', -1) == 'z'
    print('test passed')


def test_get_new_letter_step():
    assert get_new_letter(ascii_lowercase, 'd', -3) == 'a'
    assert get_new_letter(ascii_lowercase, 'a', 3) == 'd'
    print('test passed')


test_get_new_letter()
test_get_new_letter_step()