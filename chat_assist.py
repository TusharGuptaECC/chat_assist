import os
import numpy as np
import pyttsx3

os.system("cls")
print("Welcome to Tushar's menu-driven program")
pyttsx3.speak("Welcome to Tushar's menu-driven program")
print()
print("Hello, I am your assistent. I am here for your help. You can chat with me for any help")
pyttsx3.speak("Hello, I am your assistent. I am here for your help. You can chat with me for any help")
n = 1

while True:
    
    if n > 1:
        print("Please tell me what do you want to do next.")
        pyttsx3.speak("Please tell me what do you want to do next.")
    print(''' 
    Available programs
    0] exit the program
    1] Chrome
    2] command prompt
    3] excel
    4] Notepad  
    5] paint
    6] Task Manager
    7] visual studio code
    8] windows media player
    9] wordpad
      ''')
    cmd = input("please write your request here :")
    if (("not" in cmd) or ("doesn't" in cmd) or ("don't" in cmd) or ("didn't" in cmd) or ("couldn't" in cmd) or ("mustn't" in cmd) or ("wouldn't" in cmd) or ("hasn't" in cmd) or ("haven't" in cmd) or ("cannot" in cmd)):
        print("OK")
        pyttsx3.speak("OK")
    elif (("begin" in cmd) or ("start" in cmd) or ("execute" in cmd) or ("open" in cmd) or ("run" in cmd)) and (("chrome" in cmd) or ("Chrome" in cmd)):
        os.system("start chrome")
    
    elif "quit" in cmd or "exit" in cmd:
        pyttsx3.speak("have a good day")
        break
    
    elif (("begin" in cmd) or ("start" in cmd) or ("execute" in cmd) or ("open" in cmd) or ("run" in cmd)) and (("notepad" in cmd) or ("Notepad" in cmd)):
        os.system("start notepad")

    elif (("begin" in cmd) or ("start" in cmd) or ("execute" in cmd) or ("open" in cmd) or ("run" in cmd)) and (("windows media palyer" in cmd) or ("player" in cmd) or ("window player" in cmd) or ("media player" in cmd)):
        os.system("start wmplayer")
    
    elif (("begin" in cmd) or ("start" in cmd) or ("execute" in cmd) or ("open" in cmd) or ("run" in cmd) or ("view" in cmd) or ("see" in cmd)) and (("Task Manager" in cmd) or ("TaskManager" in cmd) or ("taskmanager" in cmd) or ("task manager" in cmd) or ("performance" in cmd) or ("Task manager" in cmd) ):
        os.system("Taskmgr")
    
    elif (("begin" in cmd) or ("start" in cmd) or ("execute" in cmd) or ("open" in cmd) or ("run" in cmd) or ("view" in cmd) or ("see" in cmd)) and (("Command Prompt" in cmd) or ("command prompt" in cmd) or ("cmd prompt" in cmd) or ("cmd line" in cmd)):
        os.system("conhost")

    elif (("begin" in cmd) or ("start" in cmd) or ("execute" in cmd) or ("open" in cmd) or ("run" in cmd) or ("view" in cmd) or ("see" in cmd)) and (("visual studio code" in cmd) or ("vs code" in cmd) or ("visualstudio" in cmd) or ("VS code" in cmd)):
        os.system("code")
    
    elif (("begin" in cmd) or ("start" in cmd) or ("execute" in cmd) or ("open" in cmd) or ("run" in cmd) or ("view" in cmd) or ("see" in cmd)) and (("paint" in cmd) or ("Paint" in cmd) or ("PAINT" in cmd)):
        os.system("mspaint")

    elif (("begin" in cmd) or ("start" in cmd) or ("execute" in cmd) or ("open" in cmd) or ("run" in cmd) or ("view" in cmd) or ("see" in cmd)) and (("wordpad" in cmd) or ("Wordpad" in cmd) or ("WordPad" in cmd)  or ("word pad" in cmd) or ("Word pad" in cmd) or ("Word Pad" in cmd)):
        os.system("start wordpad")

    elif (("begin" in cmd) or ("start" in cmd) or ("execute" in cmd) or ("open" in cmd) or ("run" in cmd) or ("view" in cmd) or ("see" in cmd)) and (("excel" in cmd) or ("Excel" in cmd) or ("ms excel" in cmd) or ("msexcel" in cmd) or ("MS Excel" in cmd)):
        os.system("start excel")


    else:
        print('''  ////????HELP????\\\\
            Posible reasons for failure.
            1] Program not available in the given menu. If it is available please follow point 2nd. 
            2] Please try to use 'start', 'execute', 'run' keywords in your statement.
            3] For using notepad always use capital 'N' as shown 'Notepad' ''')
        pyttsx3.speak("Posible reasons for failure. first Program not available in the given menu. If it is available please follow point second. Please try to use 'start', 'execute', 'run' keywords in your statement.")
    
    
    hold_screen = input("please press enter to continue")
    # pyttsx3.speak("please press enter to continue")
    os.system("cls")
    n = n+1

    
