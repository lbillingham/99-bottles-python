"""
code to 'sing' 99 bottles of beer, after the Metz and Owen
OOP design book

in each verse, we use
- `nth` to indicate the current number of bottles before 1 is 'taken down'
- `np1th` to indicate the number of bottles after the 'take 1 down'
- `ves` (or `ves`) to indicate the vessel name of bottles/bottle/can etc.
"""


_PART_VERSE = """
{count_now} {vessel_now} of beer on the wall, {count_now} {vessel_now} of beer.
Take {pronoun} down and pass it around, {count_next} {vessel_next} of beer on the wall.
"""


def verse(n_bottles):
    """'sing' a single verse"""
    count_next = n_bottles - 1
    vessel_now = 'bottles'
    vessel_next = vessel_now
    pronoun = 'one'
    if count_next == 1:
        vessel_next = 'bottle'
    if n_bottles == 1:
        vessel_now = 'bottle'
        count_next = 'no more'
        pronoun = 'it'
    custom_parts = dict(
        count_now=n_bottles,
        count_next=count_next,
        vessel_now=vessel_now,
        vessel_next=vessel_next,
        pronoun=pronoun
    )
    return _PART_VERSE.format_map(custom_parts)


def verses(n_bottles_start, n_bottles_end):
    """
    'sing' verses between:
    - `'n_bottles_start' bottles of beer on the wall ...'
    - `'n_bottles_end' bottles of beer on the wall ...'
    """
    bottle_range = range(n_bottles_start, n_bottles_end - 1, -1)
    return ''.join(verse(i) for i in bottle_range)

