"""
code to 'sing' 99 bottles of beer, after the Metz and Owen
OOP design book
"""

def verse(number):
    """'sing' one single verse of the song"""
    bottle_number = BottleNumber.for_(number)

    template = (f"{bottle_number}".capitalize() +
                " of beer on the wall, " +
               f"{bottle_number} of beer.\n" +
               f"{bottle_number.action}" +
               f"{bottle_number.sucessor} of beer on the wall.\n")
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

    @staticmethod
    def for_(number):
        choices = {0: BottleNumber0, 1: BottleNumber1, 6:BottleNumber6}
        class_chosen = choices.get(number, BottleNumber)
        return class_chosen(number)

    @property
    def sucessor(self):
        """
        what is next in the sequence after `number`
        """
        return BottleNumber.for_(self.number - 1)

    @property
    def container(self):
        """
        what is the drink in?
        n bottles, a bottle, 1 six-pack, some barrels?
        """
        return 'bottles'

    @property
    def action(self):
        """
        what will we do with the beer
        """
        return f"Take {self.pronoun} down and pass it around, "

    @property
    def pronoun(self):
        """
        what to sing instead of bottles/container
        in 'Take XXX down ...' part
        """
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
    def action(self):
        return "Go to the store and buy some more, "

    @property
    def quantity(self):
        return 'no more'

    @property
    def sucessor(self):
        return BottleNumber.for_(99)

class BottleNumber1(BottleNumber):
    @property
    def pronoun(self):
        return "it"

    @property
    def container(self):
        return 'bottle'

class BottleNumber6(BottleNumber):
    @property
    def container(self):
        return 'six-pack'
    @property
    def quantity(self):
        return '1'