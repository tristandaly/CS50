from adventurelib import *
from inventory import *
import time

set_context('mailbox_close')
#set_context('flag_up')


out_front = Room("""
You stand in the front yard of the big house. Its porch, to your NORTH, looks dry and dead.
There is a mailbox in the front yard and a path leading WEST.
""")


#out_front.items = Bag([Item('spoon', 'a shiny spoon')])
out_front.items= Bag([Item('spoon', 'a shiny spoon')])
