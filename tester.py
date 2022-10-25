from helper import screenHelper
from helper import minecraftScreenHelper
from helper import fileManager
import getpass
import os

print("**** DEBUG AND TESTING ****")
print("*** running as user: [%s]" % (os.getlogin() ))
print("*** Effective user is [%s]" % (getpass.getuser() ))

print("***screenHelper.get_running_screen_sessions()")
print(screenHelper.get_running_screen_sessions())

print("***screenHelper.is_session_present(minecraft)")
print(screenHelper.is_session_present("minecraft"))

print("***screenHelper.is_session_present(none)")
print(screenHelper.is_session_present("none"))

print("***minecraftScreenHelper.send_say_in_minecraft_session(I sended this using Python :D)")
print(minecraftScreenHelper.send_say_in_minecraft_session("I sended this using Python :D"))

print("***fileManager.clean_file_content_abs_path(/home/minecraft/scripts/python/minecraftlotto/testfiles, testfile1.txt)")
print(fileManager.clean_file_content_abs_path("/home/minecraft/scripts/python/minecraftlotto/testfiles", "testfile1.txt"))

print("***fileManager.clean_file_content_relative_path(testfiles, testfile1.txt)")
print(fileManager.clean_file_content_relative_path("../testfiles", "testfile1.txt"))

print("***fileManager.clean_file_content_relative_path(path=/home/minecraft/scripts/python/minecraftlotto/testfiles/,filename=testfile3.txt, destpath=/home/minecraft/scripts/python/minecraftlotto/testfiles/, destfilename=copy_existing_file_test.txt)")
print(fileManager.copy_existing_file(path="/home/minecraft/scripts/python/minecraftlotto/testfiles", 
                                    filename="testfile3.txt",
                                    destpath="/home/minecraft/scripts/python/minecraftlotto/testfiles", 
                                    destfilename="copy_existing_file_test.txt"))

print("***fileManager.copy_existing_file_and_clean_srcfile()")
print(fileManager.copy_existing_file_and_clean_srcfile(path="/home/minecraft/scripts/python/minecraftlotto/testfiles", 
                                    filename="testfile4.txt",
                                    destpath="/home/minecraft/scripts/python/minecraftlotto/testfiles", 
                                    destfilename="copy_existing_file_and_clean_srcfile.txt"))
print("***fileManager.append_content_to_file()")
print(fileManager.append_content_to_file(srcpath="/home/minecraft/scripts/python/minecraftlotto/testfiles", 
                                    srcfilename="testfile5.txt",
                                    content="[THIS SHOULD BE NOW ADDED]" + "\n" + "[AND THIS ALSO BUT IN A NEW LINE]"))

print("***fileManager.append_content_to_file() (append content from an other file")
print(fileManager.append_content_to_file(srcpath="/home/minecraft/scripts/python/minecraftlotto/testfiles", 
                                    srcfilename="testfile5.txt",
                                    content=fileManager.load_file_content_relative_path("../testfiles", "testfile2.txt")))


