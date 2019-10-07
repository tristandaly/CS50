from adventurelib import *
from out_front import *
import time


### Here lies the evil code of the mailbox
###########################################

@when('open mailbox')
def open_mailbox():
    if get_context() == 'mailbox_irrelevant':
        say("You open the mailbox.")
    elif get_context() == 'mailbox_close':
        set_context('mailbox_open')
        say("You open the mailbox.")
    else:
        say("It's already open.")

@when('close mailbox')
def close_mailbox():
    if get_context() == 'mailbox_irrelevant':
        say("You close the mailbox.")
    elif get_context() == 'mailbox_open':
        set_context('mailbox_close')
        say("You close the mailbox.")
    else:
        say("It's already closed.")

@when('look at mailbox')
def mailbox_description():
    if get_context() != 'flag_gone' or 'flag_down':
        say("Ordinary mailbox, all things considered. The flag is up.")
    elif get_context() == 'flag_down':
        say("Ordinary mailbox, all things considered. The flag is down.")
    else:
        say("Ordinary mailbox, missing its flag.")

@when('talk to mailbox')
def mailbox_conversation():
    say("""You speak at length to the mailbox until the cows come home.""")
    print()
    say("""Neither the cows nor the mailbox say anything back to you.""")

@when('punch mailbox')
def mailbox_punch():
    say("You punch the mailbox. Nothing happens")

@when('kick mailbox')
def mailbox_kick():
    if get_context() == 'mailbox_weakened':
        say("""You kick the head of the mailbox from its stand. The head and its
            contents disappear into The Void, never to be seen or rediscovered.""")
        time.sleep(2)
        say("""You like this.""")
        set_context('mailbox_destroyed')
    elif get_context() == 'mailbox_destroyed':
        say("""The mailbox is gone and you should not trouble your mind with
            such things.""")
    else:
        say("""You kick the mailbox. It is weakened.""")
        set_context('mailbox_weakened')
######################################End Code
##Flag Actions

@when('look at flag')
def flag_description():
    if get_context() is not 'flag_gone' or 'flag_down':
        say('Bright red, standard mailbox flag in the UP position.')
    elif get_context() == 'flag_gone':
        say("""There is no flag here.""")
    else:
        say('Bright red, standard mailbox flag in the DOWN position.')

@when('talk to flag')
def flag_conversation():
    if get_context() == 'flag_gone':
        say("""There is no flag here.""")
    else:
        say("""You talk at length to the red flag. Nothing happens.""")

@when('punch flag')
def flag_punch():
    if get_context() != 'flag_down'or 'flag_gone':
        say("You punch the flag into the DOWN position.")
    elif get_context() == 'flag_down':
        say("""You punch the flag back UP, dinging the mailbox in the process.""")
        set_context('mailbox_weakened')
    elif get_context() == 'mailbox_destroyed':
        say("""There's no flag if there's no mailbox!""")
    else:
        say("There is no flag here.")

@when('kick flag')
def flag_kick():
    if get_context() == 'flag_gone':
        say("""There is no flag here.""")
    elif get_context() == 'mailbox_destroyed':
        say("""You kick at the air. There is no mailbox or flag here.""")
    else:
        say("""You kick the flag with the grace of a building demolition. The flag
            flies off into Oblivion, never to be seen again.""")
        set_context('flag_gone')

###############################################################
