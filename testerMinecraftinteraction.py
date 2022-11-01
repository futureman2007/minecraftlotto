from helper import screenHelper
from helper import minecraftinteractionHelper
from helper import fileManager
import os
import getpass

print("**** DEBUG AND TESTING ****")
print("*** running as user: [%s]" % (os.getlogin() ))
print("*** Effective user is [%s]" % (getpass.getuser() ))

print("***minecraftScreenHelper.send_say_in_minecraft_session(I sended this using Python :D)")
print(minecraftinteractionHelper.send_say_in_minecraft_session("I sended this using Python :D"))

print("***minecraftinteractionHelper.read_newest_line_from_logfile(/home/minecraft/minecraft-server/vanilla_1-19-2/logs)")
print(minecraftinteractionHelper.read_newest_line_from_logfile("/home/minecraft/minecraft-server/vanilla_1-19-2/logs"))