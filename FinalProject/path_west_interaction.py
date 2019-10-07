from adventurelib import *
from porch import *
import time

@when('use key on gate')
@when('use key in gate')
@when('unlock gate with key')
@when('open gate with key')
def unlock_gate():
    item_in_inventory = inventory.take('key')
    if not item_in_inventory:
        print("You need the key!")
    else:
        say(f"You unlock the gate")
        time.sleep(1)
        say("""
            The doors swing open! You have made it! From here you can escape
            this evil place and look forward to playing much better games on
            your own free time. Rejoice! This is a victory for us all!
            """)
        time.sleep(1)
        exit()

@when('look at gate')
def gate_description():
    say("""
        The gate is of an old, gothic style. Both an appropriate and unusual
        addition to the abandoned house in the middle of the woods. Dead vines
        accent its borders. The gate is locked.
        """)

@when('talk to gate')
def gate_conversation():
    say("You talk to the gate and nothing happens.")

@when('punch gate')
def gate_punch():
    if get_context() is 'ouch':
        say("Nope.")
    else:
        say("You punch the gate and immediately regret it. Ouch.")
        set_context('ouch')

@when('kick gate')
def gate_kick():
    say("In a fit of questionable stupidity, you kick the gate.")
    say("Ouch. Nothing happens.")              
