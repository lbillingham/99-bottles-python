"""
code to 'sing' 99 bottles of beer, after the Metz and Owen
OOP design book
"""
def plural(num):
    """do we have a `'foo'` or some `'foos'`"""
    plurl = 's'
    if num == 1:
        plurl = ''
    return plurl


def verse(num_bottles):
    """'sing' one single verse of the song"""
    lyrics = (f"{num_bottles} bottles of beer on the wall, " +
              f"{num_bottles} bottles of beer.\n" +
              "Take one down and pass it around, " +
              f"{num_bottles - 1} bottle{plural(num_bottles-1)} " +
              "of beer on the wall.\n")

    return lyrics
