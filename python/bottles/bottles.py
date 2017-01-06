"""
code to 'sing' 99 bottles of beer, after the Metz and Owen
OOP design book
"""

def verse(num_bottles):
    """'sing' one single verse of the song"""
    lyrics = (f"{num_bottles} bottles of beer on the wall, " +
              f"{num_bottles} bottles of beer.\n" +
              "Take one down and pass it around, " +
              f"{num_bottles - 1} bottles of beer on the wall.\n")

    return lyrics
