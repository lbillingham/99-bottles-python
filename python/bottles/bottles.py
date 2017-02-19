"""
code to 'sing' 99 bottles of beer, after the Metz and Owen
OOP design book
"""


def verse(number):
    """'sing' one single verse of the song"""
    bottle_number = BottleNumber(number)
    next_bottle_number = BottleNumber(bottle_number.sucessor)
    template = (f"{bottle_number.quantity.capitalize()} {bottle_number.container} of beer on the wall, " +
               f"{bottle_number.quantity} {bottle_number.container} of beer.\n" +
               f"{bottle_number.action}" +
               f"{next_bottle_number.quantity} {next_bottle_number.container} of beer on the wall.\n")

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


class BottleNumber:

    def __init__(self, number):
        self.number = number

    @property
    def sucessor(self):
        """
        what is next in the sequence after `number`
        """
        if self.number == 0:
            return 99
        else:
            return self.number - 1

    @property
    def container(self):
        """
        what is the drink in?
        n bottles, a bottle, 1 six-pack, some barrels?
        """
        if self.number == 1:
            return 'bottle'
        else:
            return 'bottles'

    @property
    def action(self):
        """
        what will we do with the beer
        """
        if self.number == 0:
            return "Go to the store and buy some more, "
        else:
            return f"Take {self.pronoun} down and pass it around, "

    @property
    def pronoun(self):
        """
        what to sing instead of bottles/container
        in 'Take XXX down ...' part
        """
        if self.number == 1:
            return "it"
        else:
            return "one"

    @property
    def quantity(self):
        """
        how describe the number of bottles
        99, 98, ..., 2, 1, no more
        """
        if self.number == 0:
            return "no more"
        else:
            return str(self.number)
