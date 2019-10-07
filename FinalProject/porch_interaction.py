from adventurelib import *
from porch import *
import time

########################################################
@when('look at door')
@when('look at front door')
def front_door_description():
    if current_room == porch:
        say('test')
    else:
        say('What door?')

@when('talk to door')
@when('talk to front door')
def front_door_conversation():
    if current_room == porch:
        say("""You talk to the door, though it does not respond.""")
    else:
        say('What door?')

@when('punch door')
@when('punch front door')
def front_door_punch():
    if current_room == porch:
        say("""You punch the door with a blast of power. Nothing happens.""")
    else:
        say('What door?')

@when('kick door')
@when('kick front door')
def front_door_kick():
    if current_room == porch:
        say("""You kick the door. Nothing happens.""")
    else:
        say('What door?')
#########################################################

@when('look at left window')
@when('look in left window')
def left_window_description():
    if current_room == porch:
        if get_context() == 'super_sticky_window_situation' or get_context() == \
        'sticky_window_situation':
            say("You cannot see that far based on your current predicament.")
        else:
            say("""You see a dark kitchen with white countertop. A wooden table sits
                just to the left, and there is another room beyond, though it is too
                dark to see.""")
    else:
        say("What window?")

@when('talk to left window')
def left_window_conversation():
    if current_room == porch:
        say("""Speaking to the window isn't helping you.""")
    else:
        say('What winow?')

@when('punch left window')
def left_window_punch():
    if current_room == porch:
        say("""You punch the window, revealing that you cannot punch hard enough
            to do any damage.""")
    else:
        say('What window?')

@when('kick left window')
def left_window_kick():
    if current_room == porch:
        if get_context() == 'left_window_kicked':
            say("Nothing happens.")
        else:
            set_context('left_window_kicked')
            say("""You kick the window. A fog spreads over the entire view of the
            inside until nothing can be seen""")
    else:
        say('What window?')

#############################################

@when('look at right window')
@when('look in right window')
def right_window_description():
    if current_room == porch:
        if get_context() == 'right_window_gone':
            say("You see an accessible room to the NORTH.")
        else:
            say("""You see an empty room. No larger than a closet. Light shines only
                from the outside. You see no doors in this room.""")
    else:
        say('There are no windows here.')

@when('talk to right window')
def right_window_conversation():
    if current_room == porch:
        say("""You lean against the cold pane of abandoned glass and say "hello." """)
        time.sleep(4)
        say("""The window vibrates briefly""")
    else:
        say('There are no windows here.')

@when('punch right window')
def right_window_punch():
    if current_room == porch:
        say('You punch the window.')
        set_context('right_window_punched')
        print()
        input()
    if current_room == porch and get_context() == 'right_window_punched':
        for i in range(6):
            say("You punch the window. Do it again.")
            input()
        set_context('right_window_gone')
        say("The glass breaks.")
    else:
        say('There are no windows here.')

@when('kick right window')
def right_window_kick():
    if current_room == porch:
        if get_context() != 'sticky_window_situation' and get_context() != \
        'super_sticky_window_situation':
            set_context('sticky_window_situation')
            say("""You kick the right window. Your foot sticks to the glass like glue""")
        elif get_context() == 'sticky_window_situation':
            set_context('super_sticky_window_situation')
            say("""You kick the right window with your other foot. You slump backward
                onto the porch in shame as both feet are now stuck.""")
            time.sleep(2)
            print()
            say("""It is here where you live the rest of your days.""")
            time.sleep(2)
            exit()
    else:
        say('There are no windows here.')

#############################################

@when('look at window')
@when('look in window')
@when('look through window')
def porch_window_query():
    if current_room == porch:
        say('Which window would you like to look at?')
        print()
        window_answer = input()
        if window_answer == 'left' or 'left window':
            print()
            left_window_description()
        elif window_answer == 'right' or 'right window':
            print()
            right_window_description()
        else:
            porch_window_query()
    else:
        say('There is no window here.')
