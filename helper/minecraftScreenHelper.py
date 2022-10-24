import os
from helper import screenHelper

def send_say_in_minecraft_session(stringToSay):
    if (not stringToSay):
        print("Debug: String to say in minecraft is not right!")
        return None

    if (screenHelper.is_session_present("minecraft") == False):
        print("Debug: is_session_present in minecraft is not right!")
        return None
    #screen -s minecraft -X stuff $'say "***Starting Backup...\n'
    #ret = os.popen("screen -S minecraft -X stuff \"say ***Starting Backup\"" + "^M")
    return screenHelper.stuff_string_into_screen_session(sessionname="Minecraft", stringToStuff="say " + stringToSay + "^M" )