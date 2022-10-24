import os

#returns a list of all running screen sessions. If no session is running, returns an empty list.
def get_running_screen_sessions():
    sessions = []
    ret=os.popen('screen -ls').read().splitlines()
    
    ret.pop(0)
    ret.pop(-1)

    for strings in ret:
        sessions.append(strings.split("\t")[1])
    return sessions

#checks, if there is a session with <sessionname> if so, return true, else return false. if list is empty (no running screen session) return false
def is_session_present(sessionname):
    if (not sessionname):
        return False

    sessionname = sessionname.lower()
    listOfScreenSessions = get_running_screen_sessions()
       
    if (len(listOfScreenSessions) == 0):
        return False

    for sessions in listOfScreenSessions:
        if (sessionname in sessions.lower()):
            return True
    return False

#TODO: instead of returning False, raise an exception
#TODO: add guarantee logic if something has stuffed or errorhandling (e.g. screen is not installed, stuff has gone wrong (given, when returning the output of the stuff command))
#stuffs <stringToStuff> to an existing session named <sessionname>
#Returns the returing string after the stuff command has been executed
def stuff_string_into_screen_session(sessionname, stringToStuff):
    if (not sessionname or not stringToStuff):
        return None

    if (is_session_present == False):
        return None
    
    ret = os.popen("screen -S " + sessionname + " " + "-X stuff " + "\""+ stringToStuff + "\"").read()