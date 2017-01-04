"""
code to 'sing' 99 bottles of beer, after the Metz and Owen
OOP design book

"""

def verse(num_bottles):
    """
    'sing' a single verse from 99 bottles of beer
    - `'num_bottles' bottles of beer on the wall, 'num_bottles' of beer ...`
    """
    if num_bottles == 0:
        the_verse = """
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
"""
    elif num_bottles == 1:
        the_verse = """
1 bottle of beer on the wall, 1 bottle of beer.
Take it down and pass it around, no more bottles of beer on the wall.
"""
    elif num_bottles == 2:
        the_verse = """
2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.
"""
    else:
        template = """
{num_now} bottles of beer on the wall, {num_now} bottles of beer.
Take one down and pass it around, {num_next} bottles of beer on the wall.
"""
        custom_parts = {'num_now': num_bottles, 'num_next': num_bottles - 1}
        the_verse = template.format_map(custom_parts)
    return the_verse


def verses(num_bottles_start, num_bottles_end):
    """
    'sing' verses between:
    - `'num_bottles_start' bottles of beer on the wall ...'
    - `'num_bottles_end' bottles of beer on the wall ...'
    """
    bottle_range = range(num_bottles_start, num_bottles_end - 1, -1)
    return ''.join(verse(i) for i in bottle_range)

def song():
    """'sing' the whole 99 bottles song"""
    return verses(99, 0)