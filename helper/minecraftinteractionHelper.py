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

def give_player_item (playername, itemname, amount=1):
    if (not playername or not itemname):
        return None
    
    if (screenHelper.is_session_present("minecraft") == False):
        return None

    return screenHelper.stuff_string_into_screen_session(sessionname="minecraft", stringToStuff="give " + playername + " " + "itemname" + " " + str(amount) + "^M" )

#def
    #to get the first player which has written into the chat:
    #players2 = re.findall('<(.*?)>( !lotto (.*?)[0-9]+)', logfileContent)
    #Get any String which matches the following: <(anyString)> !lotto <anyNumber>
    #Return example: print(players2[0]):
    #('Futureman2007', ' !lotto 491', '')
    #here you can access the elements like an array again!
    #idea: 
    #   start the lotto game by cleaning the current logs (move to old_logs.log)
    #   print the message:  a new lottery will begin soon! write !lotto <number> in the chat to participate!
    #                       The number has to be between 0 and 1000!
    #                       you can only have one bet per round and your last bet will be used!
    #                       You have 10 minutes left to bet! Price: (choosen randomly from a file with prices to win (json file))
    # Then every minute: you have x minutes left to bet! Price <random>
    # when the Log has changed, Search the logs if someone has written !lotto <number>. See https://stackoverflow.com/questions/3274334/how-can-i-watch-a-file-for-modification-change to use inotify!
    # If a string is found with a bet: 
    #   check if the player has already given a bet (entry with playername already exists in the file).
    #   list (json file bets): bets: { {"Playername": <Name>, "Bet": <Number from chat>}, {"Playername" : <Name2>, "Bet:" <number from chat>
    # if so: 
    #   overwrite the bet of the player, 
    # if not: 
    #   create a new entry in the file.
    # When the logfile has changed stage: 
    #   either someone has written /!lotto <number> or not: 
    #       after the check, append the current log to the old logs (clean it up again)
    # When the Time is up, generate a random number between 0 and 1000 and print: The lotto Number is: <number>.
    # Check the json file with the bets, if someone as guessed this number.
    #   if so: give him the reward choosen at the beginning by sending give <playername> <item> <amount>
    #           print : Congratulations <Playername> you won!
    #   if not: Sadly noone guessed right. More luck next Time!
    
