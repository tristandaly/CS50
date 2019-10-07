from adventurelib import *
from accessible_room import *
from out_front import *
from porch import *
import time



@when('one')
def first_door():
    say("You open the first door and enter the room.")
    say("Your blood runs cold as you meet your only companion for the rest")
    say("of eternity.")
    time.sleep(2)
    say("""
        "Hullo FelloW!" bellows the rabbit in the top hat. You sit down and watch
        as the magic show begins.
        """)
    time.sleep(2)
    exit()

@when('two')
def second_door():
    say("You open the second door.")
    say("There before you stands a KEY upon a red hill.")
    time.sleep(2)
    say("You take the key.")
    time.sleep(1)
    inventory.add(accessible_room.items.take('key'))
    say("A portal opens to the SOUTH revealing the porch.")


@when('three')
def third_door():
    say("You open the third door...")
    time.sleep(1)
    say('and black out.')
    time.sleep(3)
    say("""
        You awaken in a small canoe, whispering down a river in a dark cave.
        The stone walls around you smell of moldy sulphur.
        Through the walls of the canoe you can sense the coldness of the water
        and you dare not leave your seat.

         The canoe makes its own way slowly down the river for two days until it
         stops at staircase that has been chisled out of the wall.

          Tired, hungry, and emotionally drained, you proceed up the stairs.

           Through a deep, dark passageway you walk until you reach a wooden door.

            Do you open the door?
            """)
    print()
    response = input()
    if response is 'yes' or 'y':
        say("""
        The door creaks open and, to your absolute terror, you are now last in
        line at the DMV of Eternity.

         The End!
         """)
        time.sleep(1)
        exit()
    else:
        say("Well that was a mistake. You are eaten by the monster.")
        time.sleep(1)
        exit()

@when('four')
def fourth_door():
    say("""
        You open the fourth door. You're pulled in by a vacuum of air and the
        door shuts behind you.

         You are now standing in the kitchen. The same kitchen seen from the window
         outside.

          On the table you see a NOTE. Do you wish to READ the NOTE?

           enter y or n
        """)
    print()
    note_answer = input()
    if note_answer is 'y':
        say("""
            The note reads:

             *Bacon

              *Paper Towels

               *Orange Joose

                *Cimanen rolls

                 """)
        say("""
            You crumple the note in your hand, underwhelmed.
        """)
    elif note_answer is 'n':
        say("You don't read the note.")
    else:
        say("Say what?")
