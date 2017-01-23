"""
code to 'sing' 99 bottles of beer, after the Metz and Owen
OOP design book
"""


def verse(number):
    """'sing' one single verse of the song"""
    template = (f"{quantity(number).capitalize()} {container(number)} of beer on the wall, " +
               f"{quantity(number)} {container(number)} of beer.\n" +
               f"{action(number)}" +
               f"{quantity(sucessor(number))} {container(sucessor(number))} of beer on the wall.\n")

    return template


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
    return BottleNumber(number).container(number)


def pronoun(number):
    """
    what to sing instead of bottles/container
    in 'Take XXX down ...' part
    """
    return BottleNumber(number).pronoun(number)

def quantity(number):
    """
    how describe the number of bottles
    99, 98, ..., 2, 1, no more
    """
    return BottleNumber(number).quantity(number)


def action(number):
    """
    what will we do with the beer
    """
    return BottleNumber(number).action(number)


def sucessor(number):
    """
    what is next in the sequence after `number`
    """
    return BottleNumber(number).sucessor(number)



class BottleNumber:

    def __init__(self, number):
        self.number = number

    def sucessor(self, number):
        """
        what is next in the sequence after `number`
        """
        if number == 0:
            return 99
        else:
            return number - 1

    def container(self, delete_me):
        """
        what is the drink in?
        n bottles, a bottle, 1 six-pack, some barrels?
        """
        if self.number == 1:
            return 'bottle'
        else:
            return 'bottles'

    def action(self, number):
        """
        what will we do with the beer
        """
        if number == 0:
            return "Go to the store and buy some more, "
        else:
            return f"Take {pronoun(number)} down and pass it around, "

    def pronoun(self, number):
        """
        what to sing instead of bottles/container
        in 'Take XXX down ...' part
        """
        if number == 1:
            return "it"
        else:
            return "one"

    def quantity(self, number):
        """
        how describe the number of bottles
        99, 98, ..., 2, 1, no more
        """
        if number == 0:
            return "no more"
        else:
            return str(number)
