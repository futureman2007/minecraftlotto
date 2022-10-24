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
#stuffs <stringToStuff> to an existing session named <sessionname>
#Returns True on success, else false.
#if one of poth parameters is emtpy, return False
#If session with specified name is not present, return false
def stuff_string_into_screen_session(sessionname, stringToStuff):
    if (not sessionname or not stringToStuff):
        return False

    if (is_session_present == False):
        return False
    ret = os.popen("screen -S " + sessionname + " " + "-X stuff " + "\""+ stringToStuff + "\"")