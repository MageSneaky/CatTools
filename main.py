import os
import sys
import platform
import psutil
import win32api
import socket
import netifaces
import tkinter as tk
import GPUtil

from time import sleep

os.system("title " + "CatTools") # sets title of cmd window

for arg in sys.argv: # le bruh
    arg = arg.lower()

options = """
0) Exit
1) Sinfo
2) WhereIs
3) Calculator
9) Help
10) Version
"""

#declarations
version_number = "1.2"
authors = ["Alex Hjortsberg", "Oskar Lindgren"]
github = "https://github.com/MageSneaky/CatTools"

# system info option
def Sinfo():
    os.system("title " + "CatTools - System Info")
    print("Please wait... Gathering system information.")
    os.system("cls")
        
    # OS
    if platform.machine()  == "AMD64":
        arch = "x64 or AMD64"
    else:
        arch = platform.machine()
        
    print(f"=========================\n\nOPERATING SYSTEM\n\nArchitecture: {arch}\nVersion: {platform.version()}\nPlatform: {platform.platform()}")
        
    # CPU
    print(f"=========================\n\nCPU\n\nName: {platform.processor()}\nCores: {psutil.cpu_count(False)}\nThreads: {psutil.cpu_count(True)}\nUsage: {psutil.cpu_percent()}%")
        
    # RAM
    print(f"=========================\n\nMEMORY\n\nTotal Physical Memory: {round(psutil.virtual_memory().total/1024/1024/1024, 2)}GB\nUsage: {psutil.virtual_memory()[2]}%")
       
    # GPU
    GPUs = GPUtil.getGPUs()
    if len(GPUs) == 1:
        gpu = GPUs[0]
        print(f"=========================\n\nGPU\n\nLoad: {round(gpu.load*100, 2)}%\nMemLoad: {round(gpu.memoryUtil*100, 2)}%\n")
    else:
        for gpu in GPUs:
            print(f"=========================\n\nGPU{gpu.id}\n\nLoad: {round(gpu.load*100, 2)}%\nMemLoad: {round(gpu.memoryUtil*100, 2)}%\n")
    
    
    # Drives
    drives = win32api.GetLogicalDriveStrings().split('\000')[:-1]
    print(f"=========================\n\nDISK\n")
    for drive in drives:
        letter = drive
        drive = f"Total: {round(psutil.disk_usage(drive).total/1024/1024/1024)}GB Used: {round(psutil.disk_usage(drive).used/1024/1024/1024)}GB Free: {round(psutil.disk_usage(drive).free/1024/1024/1024)}GB"
        print(f"{letter} | {drive}")
        
    # Network
    print(f"=========================\n\nNETWORK\n\nIPv4: {socket.gethostbyname(socket.gethostname())}\nDefault Gateway: {netifaces.gateways()['default'][netifaces.AF_INET][0]}")
      
    print("Press enter to continue")
    input()
    Start()
    
# whereis options
def WhereIs(filename=None):
    print(filename)
    sys.argv = [sys.argv[0]]
    drive = input("What drive do you want to search? (C | D | E | etc)\n")
    if(filename != None):
        lookup_name = filename
    else:
        lookup_name = input("What file do you want to look up?\n")

    try:
        os.chdir(drive+":\\")
    except Exception():
        print("you didn't input a drive correctly!")
        input("Enter to return")
        Start()

    print("Searching...", end="\r")

    c_drive_dirs = [curdir for curdir, _, _ in os.walk(os.getcwd())]

    print("Locating...", end="\r")

    number = -1
    for thing in c_drive_dirs:
        number+=1
        try:
            os.chdir(c_drive_dirs[number])
        except OSError:
            continue
        files = os.listdir()
        for cur in files:
            if cur.__contains__(lookup_name):
                print("Found file at " + str(os.getcwd()) + "\\" + cur)
    print("Press enter to continue")
    input()
    Start()
    

# help option
def Help():
    os.system("title " + "CatTools - Help")
    print(f"Commands")
    print(f"help, h - Displays commands and options")
    print(f"version, v - Displays program version")
    print(f"sinfo - Displays system information")
    print(f"whereis FILENAME - Finds path(s) to file searched for")
    print(f"calculator, calc - Opens a simple calculator")
    print(f"\n{github}\nMade by: {' & '.join(authors)}")
    
    print("Press enter to continue")
    input()
    Start()
      
def Calculator():
    print("Press q to exit")
    print("[Uses python syntax]")
    while True:
        userinput = input("Equaction: ")
        if userinput.lower() == 'q':
            print("test")
            Start()
        else:
            try:
                print(eval(userinput))
            except Exception as e:
                print(e)
                input("Press enter to continue")
                Start()
    

# Version option
def Version():
    os.system("title " + "CatTools - Version")
    print(f"Version: {version_number}\n")
    
    print("Press enter to continue")
    input()
    Start()


# main runtime     
def Start():
    os.system("cls")
    if len(sys.argv) < 2:
        os.system("title " + "CatTools")
        print("Select a tool:")
        print(options)
        
        selection = int(input())
        
        if selection == 0:
            os.system("cls")
            exit()
        elif selection == 1:
            os.system("cls")
            Sinfo()
        elif selection == 2:
            os.system("cls")
            WhereIs()
        elif selection == 3:
            os.system("cls")
            Calculator()
        elif selection == 9:
            os.system("cls")
            Help()
        elif selection == 10:
            os.system("cls")
            Version()
        else:
            print("BRUH")
        
    elif any(sys.argv[1] == s for s in ["sinfo"]):
        os.system("cls")
        sys.argv = [sys.argv[0]]
        Sinfo()   
    elif any(sys.argv[1] == s for s in ["calc", "calculator"]):
        os.system("cls")
        sys.argv = [sys.argv[0]]
        Calculator()        
    elif any(sys.argv[1] == s for s in ["help", "h"]):
        os.system("cls")
        sys.argv = [sys.argv[0]]
        Help()  
    elif any(sys.argv[1] == s for s in ["version", "v"]):
        os.system("cls")
        sys.argv = [sys.argv[0]]
        Version()
    elif any(sys.argv[1] == s for s in ["whereis"]):
        if len(sys.argv) > 1:
            os.system("cls")
            WhereIs(sys.argv[2])
        else:
            os.system("cls")
            WhereIs()
        

# run
Start()