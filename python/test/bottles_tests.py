"""
tests for our code that is supposed to 'sing'
the 99 bottles of beer song
after the Metz and Owen
OOP design book
but in python
"""
from bottles import bottles


def test_99_bottles_verse():
    """
    can we 'sing' the verse beginning
    '99 bottles of beer on the wall, 99 bottles of beer ...'
    """
    expected = ("99 bottles of beer on the wall, " +
                "99 bottles of beer.\n" +
                "Take one down and pass it around, " +
                "98 bottles of beer on the wall.\n")
    assert expected == bottles.verse(99)


def test_3_bottles_verse():
    """can wwe 'sing' verse '3 bottles of beer ...'"""
    expected = ("3 bottles of beer on the wall, " +
                "3 bottles of beer.\n" +
                "Take one down and pass it around, " +
                "2 bottles of beer on the wall.\n")
    assert expected == bottles.verse(3)


def test_2_bottles_verse():
    """
    can we 'sing' verse '2 bottles of beer ...'
    we're going to have to deal with pluralization
    """
    expected = ("2 bottles of beer on the wall, " +
                "2 bottles of beer.\n" +
                "Take one down and pass it around, " +
                "1 bottle of beer on the wall.\n")
    assert expected == bottles.verse(2)

def test_1_bottles_verse():
    """
    can we 'sing' verse '1 bottle of beer ...'
    we're going to have to deal
    - pluralization
    - 'no more',
    - 'take _it_ down'
    """
    expected = ("1 bottle of beer on the wall, " +
                "1 bottle of beer.\n" +
                "Take it down and pass it around, " +
                "No more bottles of beer on the wall.\n")
    assert expected == bottles.verse(1)
