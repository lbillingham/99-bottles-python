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
