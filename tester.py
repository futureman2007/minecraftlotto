from helper import screenHelper
from helper import minecraftScreenHelper
from helper import fileManager

print("**** DEBUG AND TESTING ****")

print("***screenHelper.get_running_screen_sessions()")
print(screenHelper.get_running_screen_sessions())

print("***screenHelper.is_session_present(minecraft)")
print(screenHelper.is_session_present("minecraft"))

print("***screenHelper.is_session_present(none)")
print(screenHelper.is_session_present("none"))

print("***minecraftScreenHelper.send_say_in_minecraft_session(I sended this using Python :D)")
print(minecraftScreenHelper.send_say_in_minecraft_session("I sended this using Python :D"))

print("***")
print(fileManager.clean_file_content_abs_path("/home/minecraft/testfile.txt"))

print(copy_existing_file)

