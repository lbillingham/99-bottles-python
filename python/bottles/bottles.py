"""
code to 'sing' 99 bottles of beer, after the Metz and Owen
OOP design book
"""


def verse(num_bottles):
    """'sing' one single verse of the song"""
    switcher = {
    0: ("No more bottles of beer on the wall, " +
        "no more bottles of beer.\n" +
        "Go to the store and buy some more, " +
        "99 bottles of beer on the wall.\n"),
    1: ("1 bottle of beer on the wall, " +
        "1 bottle of beer.\n" +
        "Take it down and pass it around, " +
        "no more bottles of beer on the wall.\n"),
    2: ("2 bottles of beer on the wall, " +
        "2 bottles of beer.\n" +
        "Take one down and pass it around, " +
        "1 bottle of beer on the wall.\n")
    }
    default = (f"{num_bottles} bottles of beer on the wall, " +
               f"{num_bottles} bottles of beer.\n" +
               "Take one down and pass it around, " +
               f"{num_bottles - 1} bottles of beer on the wall.\n")

    return switcher.get(num_bottles, default)


def verses(_, __):
    """'sing' several verses of song from `_` to `__`"""
    lyrics = verse(99) + "\n" + verse(98)
    return lyrics
