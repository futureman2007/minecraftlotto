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
    
    listOfScreenSessions = get_running_screen_sessions()
       
    if (listOfScreenSessions.len() == 0):
        return False

    for sessions in listOfScreenSessions:
        if (sessions in sessionname):
            return True
    return False