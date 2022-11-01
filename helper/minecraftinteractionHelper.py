import os
from helper import screenHelper
from helper import fileManager 

def send_say_in_minecraft_session(stringToSay):
    if (not stringToSay):
        return None

    if (screenHelper.is_session_present("minecraft") == False):
        return None
    #screen -s minecraft -X stuff $'say "***Starting Backup...\n'
    #ret = os.popen("screen -S minecraft -X stuff \"say ***Starting Backup\"" + "^M")
    return screenHelper.stuff_string_into_screen_session(sessionname="minecraft", stringToStuff="say " + stringToSay + "^M" )

def read_newest_line_from_logfile(pathToLogFile, filename="latest.log"):
    if (not pathToLogFile):
        return None

    logfileContent = fileManager.load_file_content_abs_path(pathToLogFile, filename)
    splitString = logfileContent.split("\n")
    return splitString[ len(splitString) -2 ]    


