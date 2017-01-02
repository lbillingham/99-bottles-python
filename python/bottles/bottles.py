"""
code to sing 99 bottles of beer, after the Metz and Owen
OOP design book
"""

PART_VERSE = """
{n_bottles} bottles of beer on the wall, {n_bottles} bottles of beer.
Take one down and pass it around, {n_bottles_minus_1} bottles of beer on the wall.
"""

def verse(n_bottles):
    """'sing' a single verse"""
    fewer_bottles = n_bottles - 1
    custom_parts = dict(
        n_bottles=n_bottles,
        n_bottles_minus_1=fewer_bottles
    )
    return PART_VERSE.format_map(custom_parts)
