"""
code to 'sing' 99 bottles of beer, after the Metz and Owen
OOP design book
"""

def verse(num_bottles):
    """'sing' one single verse of the song"""
    if num_bottles == 99:
        lyrics = ("99 bottles of beer on the wall, " +
                  "99 bottles of beer.\n" +
                  "Take one down and pass it around, " +
                  "98 bottles of beer on the wall.\n")
    else:
        lyrics = ("3 bottles of beer on the wall, " +
                  "3 bottles of beer.\n" +
                  "Take one down and pass it around, " +
                  "2 bottles of beer on the wall.\n")
    return lyrics
