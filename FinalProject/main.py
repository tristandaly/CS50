import adventurelib
from map import *
from inventory import *
from out_front import *
from out_front_interaction import *
from path_west import *
from path_west_interaction import *
from porch import *
from porch_interaction import *
from accessible_room import *
from accessible_room_interaction import *
import os
import time

# Clears screen depending on player's OS
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


@when('take ITEM')
def take(item):
    item_available = current_room.items.take(item)
    if not item_available:
        print("There is nothing here.")
    elif get_context() is 'mailbox_close' and current_room is out_front:
        print("There is nothing here.")
    else:
        inventory.add(item_available)
        print(f"You take the {item_available}.")

@when('drop ITEM')
def drop(item):
    item_in_inventory = inventory.take(item)
    if not item_in_inventory:
        print("There is nothing to drop.")
    else:
        current_room.items.add(item_in_inventory)
        print(f"You drop the {item}.")


@when("give ITEM to RECIPIENT")
def give(item, recipient):
    print(f"You give the {item} to the {recipient}.")


@when('look')
def look():
    say(current_room)

@when('use toilet')
def use_toilet():
    if get_context() != 'door_closed':
        print("You must first close the door!")
    else:
        print("Atta boy!")

@when('close DOOR')
@when('close the DOOR')
def close(door):
    set_context('door_closed')
    say(f"You close the {door}.")


@when('north', direction='north')
@when('go north', direction='north')
@when('south', direction='south')
@when('go south', direction='south')
@when('east', direction='east')
@when('go east', direction='east')
@when('west', direction='west')
@when('go west', direction='west')
@when('go within', direction='within')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        print(f"You go {direction}.")
        print()
        look()
    else:
        print(f"You can't go that way!")




if __name__ == "__main__":
    current_room = out_front
    print("""
          In this game, use the following VERBS to interact with the world:
          "look at"
          "talk to"
          "pick up"
          "punch"
          "kick"
          "use"
          ~~~~~~~~~
          Use the VERBS first, followed by the OBJECT in question. The "use"
          command can be phrased as "use OBJECT" or as "use OBJECT with OBJECT"
          ~~~~~~~~~
          To move around in the world, use the following DIRECTION COMMANDS:
          "go north"
          "go south"
          "go east"
          "go west"
          ~~~~~~~~~
          The cardinal directions can also be entered without "go" in order to
          travel.
          ~~~~~~~~~
          To access this list of commands again, type "help" at any time.
          """)
    time.sleep(3)
    #print("Are you ready to begin? y/n")
    #input()
    y_n_answer = None
    while y_n_answer != 'y' or 'n':
        #print("Are you ready to begin? y/n\n")
        y_n_answer = input("Are you ready to begin? y/n\n")
        if y_n_answer == 'y':
            clear()
            say(current_room)
            print()
            start()
        if y_n_answer == 'n':
            say("............okay\n")
            time.sleep(2)
            print()
            #print("Are you ready now?")
            y_n_answer = input("Are you ready now? y/n\n")
            if y_n_answer == 'y':
                clear()
                say(current_room)
                print()
                start()
            if y_n_answer == 'n':
                say("............okay")
                time.sleep(2)
                print()
                say("Bye!")
                exit()



#start()
