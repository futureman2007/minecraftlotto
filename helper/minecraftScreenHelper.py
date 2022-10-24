import os
from helper import screenHelper

def send_say_in_minecraft_session(stringToSay):
    if (not stringToSay):
        return None

    if (screenHelper.is_session_present("minecraft") == False):
        return None
    #screen -s minecraft -X stuff $'say "***Starting Backup...\n'
    #ret = os.popen("screen -S minecraft -X stuff \"say ***Starting Backup\"" + "^M")
    return screenHelper.stuff_string_into_screen_session(sessionname="Minecraft", stringToStuff="say " + stringToSay + "^M" )