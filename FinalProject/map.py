from adventurelib import *
from out_front import *
from path_west import *
from porch import *
from accessible_room import *
from accessible_room_interaction import *
from porch_interaction import *

out_front.west = path_west
out_front.north = porch
porch.north = accessible_room
