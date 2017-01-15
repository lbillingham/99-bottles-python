"""
code to 'sing' 99 bottles of beer, after the Metz and Owen
OOP design book
"""


def verse(number):
    """'sing' one single verse of the song"""
    switcher = {
    0: ("No more bottles of beer on the wall, " +
        "no more bottles of beer.\n" +
        "Go to the store and buy some more, " +
        "99 bottles of beer on the wall.\n"),
    1: ("1 bottle of beer on the wall, " +
        "1 bottle of beer.\n" +
        "Take it down and pass it around, " +
        "no more bottles of beer on the wall.\n") #,
    }
    default = (f"{number} bottles of beer on the wall, " +
               f"{number} bottles of beer.\n" +
               "Take one down and pass it around, " +
               f"{number - 1} {container(number - 1)} of beer on the wall.\n")

    return switcher.get(number, default)


def verses(starting, ending):
    """
    'sing' several verses of song from `starting` to `ending`
    """
    verse_range = range(starting, ending - 1, -1)
    lyrics = "\n".join(verse(n) for n in verse_range)
    return lyrics

def song():
    """'sing' the entire 99 bittles _song_"""
    return verses(99, 0)


def container(number):
    """
    what is the drink in?
    n bottles, a bottle, 1 six-pack, some barrels?
    """
    if number == 1:
        return 'bottle'
    else:
        return 'bottles'
