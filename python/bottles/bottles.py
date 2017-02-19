"""
code to 'sing' 99 bottles of beer, after the Metz and Owen
OOP design book
"""

def bottle_number_for(number):
    """factory for choosing correct BottleNumber"""
    if number == 0:
        cls_wanted = BottleNumber0
    else:
        cls_wanted = BottleNumber
    return cls_wanted(number)


def verse(number):
    """'sing' one single verse of the song"""
    bottle_number = bottle_number_for(number)
    next_bottle_number = bottle_number_for(bottle_number.sucessor)

    template = (f"{bottle_number}".capitalize() +
                " of beer on the wall, " +
               f"{bottle_number} of beer.\n" +
               f"{bottle_number.action}" +
               f"{next_bottle_number} of beer on the wall.\n")
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

    def __str__(self):
        return f'{self.quantity} {self.container}'

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
        return str(self.number)


class BottleNumber0(BottleNumber):
    @property
    def quantity(self):
        return 'no more'