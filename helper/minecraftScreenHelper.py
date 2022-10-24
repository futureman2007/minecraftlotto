import os
from helper import screenHelper

def send_say_in_minecraft_session(stringToSay):
    if (not stringToSay):
        return False

    if (screenHelper.is_session_present == False):
        return False
    #screen -s minecraft -X stuff $'say "***Starting Backup...\n'
    #ret = os.popen("screen -S minecraft -X stuff \"say ***Starting Backup\"" + "^M")
    ret = screenHelper.stuff_string_into_screen_session(sessionname="Minecraft", stringToStuff="say " + stringToSay + "^M" )
    