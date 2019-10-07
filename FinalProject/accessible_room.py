from adventurelib import *
from inventory import *
import time

accessible_room = Room("""
                       You are in a dark coffin. The window behind you shrinks,
                       and all light and warmth disappears. You feel the floor
                       beneath you begin to move down as you leave the surface
                       behind you.

                       You look around.

                       You are in a red cave. Four stone doors stand before you.

                       There is no way back up. Which door do you open?

                        one two three four
                       """)


accessible_room.items = Bag([Item('key')])
