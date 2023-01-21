"""Semi-broken, I think?"""

#######################################################
import glob
import os
import shutil
import subprocess
import sys
import time
from threading import *
#######################################################

#######################################################
from colorama import Fore
from rich.traceback import install
from rich.console import Console
from rich import *
#######################################################

#######################################################
from dependencies.divider import divider
from dependencies.loadingMessage import *
from dependencies.openingSFX import openingSFX
from dependencies.secretMenuAssets import *
from dependencies.terminalClear import terminalClear
from dependencies.playVideo import playVideo
#######################################################

def pyflix():

    install()
    console = Console()
    openingSound = Thread(target=openingSFX, daemon=True)
    openingSound.start()
    
    time.sleep(0.0008)

    openingAnimation(0.24)
    openingAnimationPt2(0.08)

    if os.path.exists(".\\settings\\settings.py"):
        with open(".\\settings\\settings.py", "r") as file:
            fullscreenPreference = file.read()
    else:
        fullscreenPreference = True

    #######################################################
    if os.path.exists(".\\Movies") == False:

        time.sleep(0.75)
        print("\n")
        divider()
        
        console.print("It looks like it is the first time you are using [yellow]Py[/][blue]flix[/].")
        time.sleep(0.75)
        console.print(f"Please wait while [yellow]Py[/][blue]flix[/] finishes the setup...")
        time.sleep(0.75)
        divider()
        rgbLoadingBar(0.75)
        console.print("[yellow]Setup Complete![/]")
        time.sleep(0.5)
        console.print("[yellow]Launching pyflix now.[/]")
        time.sleep(1)

        try:
            os.system("mkdir Movies")
        except:
            subprocess.call(["mkdir", "Movies"])
    #######################################################

    terminalClear(1)

    loop = True

    while loop == True:
        #######################################################
        print(f"""                   ~~[yellow]Py[/][blue]flix[/]~~
[red]%%>==========================================<%%[/]
[yellow]|[/] 1. Watch Movie                               [yellow]|[/]
[yellow]|[/] 2. List all Movies                           [yellow]|[/]
[yellow]|[/] 3. Add Movies from Directory                 [yellow]|[/]
[yellow]|[/] 4. Settings                                  [yellow]|[/]
[yellow]|[/] 5. Exit                                      [yellow]|[/]                                  
[red]%%>==========================================<%%[/]
        """)
        #######################################################

        userInput = console.input(f"What [yellow]mode[/] do you want to select? [yellow](1-5)[/] -> ")
        
        #######################################################
        if userInput == "1" or userInput == 1:

            terminalClear(0.75)
            movieName = console.input(f"What is the name of the movie you want to view? [yellow](Case Sensitive)[/] -> ")

            if os.path.exists(f".\\Movies\\{movieName}.mp4") and fullscreenPreference == True:
                playVideo(fr".\\Movies\\{movieName}.mp4")
                terminalClear(0.75)
            
            if os.path.exists(f".\\Movies\\{movieName}.mp4"):
                playVideo(fr".\\Movies\\{movieName}.mp4")
                terminalClear(0.75)

            else:
                terminalClear(0)
                print(f"[red]ERROR: An error occured when trying to open {movieName}.mp4![/]")
                terminalClear(1)
                continue
        #######################################################

        #######################################################
        if userInput == "2" or userInput == 2:

            terminalClear(0)
            print(f"                                                ~~[yellow]MOVIE LIST[/]~~")
            divider()
            if len(os.listdir(".\\Movies\\")) == 0:
                print(f"[yellow]It seems you haven't added any movies yet to your movie folder yet.[/]")
            
            elif len(os.listdir(".\\Movies\\")) > 10:
                for movies in os.listdir(".\\Movies\\"):
                    rgbLoadingBar(0.025)
                    print(f"[yellow]{movies :10}[/]")
            
            else:
                for movies in os.listdir(".\\Movies\\"):
                    rgbLoadingBar(0.065)
                    print(f"[yellow]{movies :10}[/]")

            divider()
            exitPrompt = console.input(f"Do you want to return to the main menu now? [yellow](Y/N)[/] -> ").title()

            if exitPrompt == "Y" or exitPrompt == "Yes":
                terminalClear(0)
                loadingBar(0.15)
                terminalClear(0.2)
                continue

            if exitPrompt == "N" or exitPrompt == "No":

                divider()
                time.sleep(5)
                exitPrompt = exitPrompt = console.input(f"Do you want to return to the main menu now? [yellow](Y/N)[/] -> ").title()

            terminalClear(0.75)
        #######################################################

        #######################################################
        if userInput == "3" or userInput == 3:

            terminalClear(0.5)

            movieName = console.input(f"What is the name of the movie you want to add? [yellow](Case Sensitive)[/] -> ")

            terminalClear(0.25)

            print(f"[yellow]Finding file please wait...[/]")

            OSNAME = os.getlogin()
             # Attempting to get valid directory
            files = glob.glob(fr"C:\\users\\{OSNAME}\\**\\*", recursive=True)                

            for file in files:
                if movieName in file:
                    rgbLoadingBar(0.3)
                    print(f"[yellow]Successfully found {movieName}.mp4![/]")
                    time.sleep(0.3)
                    try:
                        shutil.copy(file, f".\\Movies\\{movieName}.mp4")
                        print(f"[yellow]Successfully copied ({movieName}.mp4)![/]")
                        terminalClear(1)
                        continue
                    except:
                        print(f"[red]ERROR: Failed to copy ({movieName}.mp4) to target folder...[/]")
                        terminalClear()
        #######################################################

        #######################################################
        if userInput == "4" or userInput == 4:

            settingLoop = True

            while settingLoop == True:

                terminalClear(0.5)

                print(f"""[yellow]1.[/] Open video in fullscreen at start time
[yellow]2.[/] Return to Menu
                """)

                menuSetting = console.input(f"What [yellow]mode[/] do you want to select? [yellow](1-2)[/] -> ")

                if menuSetting == "1" or menuSetting == 1:

                    terminalClear(0.5)

                    userInput = console.input(f"Do you want to [yellow]prioritize[/] fullscreen mode at watch time? [yellow](Y/N)[/] -> ").title()

                    if userInput == "Y" or userInput == "Yes":

                        fullscreenPreference = "True"

                        if os.path.exists(".\\settings"):
                            with open(".\\settings\\settings.py", "w")as file:
                                file.write(fullscreenPreference)
                            print(f"{Fore.GREEN}NOTE: Your change will take effect the next time Pyflix is opened.[/]")
                            time.sleep(0.75)
                        else:
                            try:
                                os.system("mkdir settings")
                                with open(".\\settings\\settings.py", "w")as file:
                                    file.write(fullscreenPreference)
                            except:
                                subprocess.call(["mkdir", "settings"])
                                with open(".\\settings\\settings.py", "w")as file:
                                    file.write(fullscreenPreference)
                    
                    if userInput == "N" or userInput == "No":

                        fullscreenPreference = "False"

                        if os.path.exists(".\\settings"):
                            with open(".\\settings\\settings.py", "w")as file:
                                file.write(fullscreenPreference)
                            print(f"{Fore.GREEN}NOTE: Your change will take effect the next time Pyflix is opened.[/]")
                            time.sleep(0.75)
                        else:
                            try:
                                os.system("mkdir settings")
                                with open(".\\settings\\settings.py", "w")as file:
                                    file.write(fullscreenPreference)
                            except:
                                subprocess.call(["mkdir", "settings"])
                                with open(".\\settings\\settings.py", "w")as file:
                                    file.write(fullscreenPreference)
                        
                            
                if menuSetting == "2" or menuSetting == 2:

                    terminalClear(0)
                    settingLoop = False
                    loadingBar(0.15)
                    terminalClear(0.1)
                
                if menuSetting == "3" or menuSetting == 3:

                    secretMenuLoop = True

                    while secretMenuLoop == True:

                        terminalClear(0.5)
                        
                        secretMenu()

                        userInput = console.input(f"\nWhat [red]mode[/] do you want to select? [red](1-4)[/] -> ")

                        if userInput == "1" or userInput == 1:

                            openingSound = Thread(target=secretOpeningSound, daemon=True)
                            openingSound.start()
                            
                            time.sleep(0.0008)

                            secretOpeningAnimation(0.24)
                            secretOpeningAnimationPt2(0.08)
                            time.sleep(0.1)

                        if userInput == "2" or userInput == 2:

                            terminalClear(0.5)
                            speed = float(console.input(f"[red]Speed:[/] "))
                            secretLoadingBar(speed)
                            print(f"[red]Done![/]")
                            time.sleep(0.1)
                        
                        if userInput == "3" or userInput == 3:

                            terminalClear(0)
                            print(f"[red]Playing...[/]")
                            playsound(r"./assets/openingSFX.mp3")
                            terminalClear(0.45)
                        
                        if userInput == "4" or userInput == 4:
                            terminalClear(0)
                            print(f"[red]Exiting Secret Menu Now.[/]")
                            secretMenuLoop = False
        #######################################################

        #######################################################
        if userInput == "5" or userInput == 5:

            terminalClear(0)
            exitingAnimation(0.24)
            time.sleep(0.2)
            loop = False
        #######################################################

        
if __name__ == "__main__":
    pyflix()