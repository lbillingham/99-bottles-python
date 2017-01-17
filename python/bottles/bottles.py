"""
code to 'sing' 99 bottles of beer, after the Metz and Owen
OOP design book
"""


def verse(number):
    """'sing' one single verse of the song"""
    switcher = {
    0: (f"{str(quantity(number)).capitalize()} bottles of beer on the wall, " +
        "no more bottles of beer.\n" +
        "Go to the store and buy some more, " +
        "99 bottles of beer on the wall.\n")
    }
    default = (f"{quantity(number)} {container(number)} of beer on the wall, " +
               f"{number} {container(number)} of beer.\n" +
               f"Take {pronoun(number)} down and pass it around, " +
               f"{quantity(number - 1)} {container(number - 1)} of beer on the wall.\n")

    return switcher.get(number, default)


def verses(starting, ending):
    """
    'sing' several verses of song from `starting` to `ending`
    """
    verse_range = range(starting, ending - 1, -1)
    lyrics = "\n".join(verse(n) for n in verse_range)
    return lyrics


def song():
    """'sing' the entire 99 bottles _song_"""
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


def pronoun(number):
    """
    what to sing instead of bottles/container
    in 'Take XXX down ...' part
    """
    if number == 1:
        return "it"
    else:
        return "one"

def quantity(number):
    """
    how describe the number of bottles
    99, 98, ..., 2, 1, no more
    """
    if number == 0:
        return "no more"
    else:
        return number

