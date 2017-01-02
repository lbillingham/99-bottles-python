"""
code to 'sing' 99 bottles of beer, after the Metz and Owen
OOP design book

in each verse, we use
- `nth` to indicate the current number of bottles before 1 is 'taken down'
- `np1th` to indicate the number of bottles after the 'take 1 down'
- `ves` (or `ves`) to indicate the vessel name of bottles/bottle/can etc.
"""

PART_VERSE = """
{num_ves_nth} {ves_nth} of beer on the wall, {num_ves_nth} {ves_nth} of beer.
Take {pronoun} down and pass it around, {num_ves_n1th} {ves_np1th} of beer on the wall.
"""

def verse(n_bottles):
    """'sing' a single verse"""
    fewer_bottles = n_bottles - 1
    vessel_now = 'bottles'
    vessel_next = vessel_now
    pronoun = 'one'
    if fewer_bottles == 1:
        vessel_next = 'bottle'
    if n_bottles == 1:
        vessel_now = 'bottle'
        fewer_bottles = 'no more'
        pronoun = 'it'
    custom_parts = dict(
        num_ves_nth=n_bottles,
        num_ves_n1th=fewer_bottles,
        ves_nth=vessel_now,
        ves_np1th=vessel_next,
        pronoun=pronoun
    )
    return PART_VERSE.format_map(custom_parts)
