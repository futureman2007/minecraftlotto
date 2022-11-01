from helper import screenHelper
from helper import minecraftinteractionHelper
from helper import fileManager
import os
import getpass

print("**** DEBUG AND TESTING ****")
print("*** running as user: [%s]" % (os.getlogin() ))
print("*** Effective user is [%s]" % (getpass.getuser() ))

print("***screenHelper.get_running_screen_sessions()")
print(screenHelper.get_running_screen_sessions())

print("***screenHelper.is_session_present(minecraft)")
print(screenHelper.is_session_present("minecraft"))

print("***screenHelper.is_session_present(none)")
print(screenHelper.is_session_present("none"))
