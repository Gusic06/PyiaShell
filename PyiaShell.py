
from rich.console import Console
from rich import *
from rich.panel import Panel
from rich.traceback import *

import os
import subprocess
import sys

import time
from threading import *
import importlib
import getpass
from cryptography.fernet import Fernet

from apps.pyflix.pyflix import pyflix
from apps.youtube_dl.youtube import YoutubeDL
from apps.youtube_dl.youtube_dl import youtube_dl
from dependencies.commands import commands
from dependencies.check_time_settings import check_time_settings
from dependencies.command_list import command_list


def PyiaShell():

    install()
    console = Console()

    OSNAME = os.getlogin()

    os.system("cls")

    console.print(Panel("[bold][yellow]Welcome![/]\n\nUse [yellow]help[/] to learn what commands are available.[/]", title_align="center", title="[bold][blue]Py[/][yellow]thonia[/]", border_style=""))
    current_directory = os.curdir
    loop_back_directory = os.getcwd()
    root_file_directory = f"{os.curdir}\\root\\password.txt"
    root_access: bool = False

    while True:

        time_setting = check_time_settings("-") # Giving the function a none value to get an output

        current_date = time.strftime("%d/%m/%y") if time_setting == "EU" else time.strftime("%m/%d/%y")
        current_directory = '~' if current_directory == "." else current_directory
        
        if root_access is True:
            console.print(f"\n[bold][red]root@{OSNAME} | {current_directory} | [{current_date}][/]")
            user_input = console.input("[bold][red]> [/]")
        if root_access is False:
            console.print(f"\n[bold][green]pyia@{OSNAME} | [yellow]{current_directory}[/] | [{current_date}][/]")
            user_input = console.input("[bold]> [/]")
        
        user_input = user_input.split(" ", 4)
        
        if user_input[0] == "run":
            if ".py" in user_input[1] and os.path.exists(user_input[1]):
                try:
                    os.system(f"py {user_input[1]}")
                except Exception:
                    try:
                        subprocess.call(["py", f"{user_input[1]}"])
                    except:
                        console.log("[bold][red]Err[/]")

        
        if user_input[0] == "help":
            console.print(commands)


        if user_input[0] in ("clear", "cls"):
            os.system("cls")

        
        if user_input[0] == "root":
            _dir = current_directory.replace("~", ".") # Temporarily storing the current directory in a variable so it can be used later
            os.chdir(loop_back_directory)
                
            try:
                if user_input[1] in ("-e", "--exit") and root_access is True:
                    root_access: bool = False
                    os.system("cls")
                    os.chdir(loop_back_directory)
                    os.chdir(_dir)
                    continue
                if user_input[1] in ("-e", "--exit") and root_access is False:
                    console.log("[bold][red]You don't have root access![/]")
                    os.chdir(loop_back_directory)
                    os.chdir(_dir)
                    continue
                if user_input[1] not in ("-e", "--exit") and root_access is True:
                    console.log("[bold][red]You already have root access![/]")
                    os.chdir(loop_back_directory)
                    os.chdir(_dir)
                    continue
            except IndexError:
                if root_access is True:
                    console.log("[bold][red]You already have root access![/]")
                    os.chdir(loop_back_directory)
                    os.chdir(_dir)
                    continue
                else:
                    os.chdir(loop_back_directory)
                    os.chdir(_dir)
                    pass

            if os.path.exists(fr"{loop_back_directory}\\root") is False:
                os.system("cls")

                console.log("[bold][red]A root password has not been set yet.[/]")
                console.print("[bold][red]Please set a password.[/]", highlight=True)
                console.print("[bold][red]> [/]", end="")
                root_password = getpass.getpass("")

                os.mkdir("root")

                with open(fr"{loop_back_directory}\\root\\password.txt", "w") as file:
                    file.write(root_password)

                os.chdir(loop_back_directory)
                os.chdir(_dir)
                os.system("cls")

            if os.path.exists(fr"{loop_back_directory}\\root\\password.txt"):

                os.system("cls")

                console.print("[bold][red]Please enter your password.[/]")
                console.print("[bold][red]> [/]", end="")
                root_password = getpass.getpass("")

                if os.path.exists(fr"{loop_back_directory}\\key\\KEY.key") is False:
                    KEY = Fernet.generate_key()
                    os.mkdir("key")
                    with open(fr"{loop_back_directory}\\key\\KEY.key", "wb") as file:
                        file.write(KEY)
                if os.path.exists(fr"{loop_back_directory}\\key\\KEY.key"):
                    with open(fr"{loop_back_directory}\\key\\KEY.key", "rb") as file:
                        _key = file.read()
                    KEY = Fernet(_key)

                with open(fr"{loop_back_directory}\\root\\password.txt", "rb") as file:
                    encrypted_password = file.read()

                root_password_from_file = KEY.decrypt(encrypted_password)
                _password = KEY.encrypt(root_password_from_file)

                with open(fr"{loop_back_directory}\\root\\password.txt", "wb") as file:
                    file.write(_password)

                if root_password == root_password_from_file:
                    root_access: bool = True
                if root_password != root_password_from_file:
                    os.system("cls")

                    console.print("[bold][red]Incorrect password![/]")
                    time.sleep(1.5)

                os.chdir(loop_back_directory)
                os.chdir(_dir)
                os.system("cls")


        if user_input[0] == "pyvim":

            try:
                if os.path.exists(user_input[1]) and ".py" in user_input[1]:
                    try:
                        os.system(f"pyvim {user_input[1]}")
                    except PermissionError:
                        try:
                            subprocess.call(["pyvim", user_input[1]])
                        except PermissionError:
                            console.log(f"[bold][red]PermissionError: Unable to open {user_input[1]}[/]")
            except IndexError:
               try:
                   os.system("pyvim")
               except PermissionError:
                   try:
                       subprocess.call(["pyvim"])
                   except PermissionError:
                       console.log("[bold][red]PermissionError: Unable to open pyvim[/]")


        if user_input[0] in ("youtube-dl", "Youtube-DL"):
            try:
                main = YoutubeDL(2)
                try:
                    youtubeDl(user_input[1])
                except IndexError:
                    main.run("[bold][yellow]Link: [/]", 2)
                os.system("cls")
            except Exception:
                pass


        if user_input[0] == "pip" and root_access is True:

            if user_input[1] == "install":
                try:
                    subprocess.call(["py", "-m", "pip", "install", f"{user_input[2]}"])
                except ModuleNotFoundError:
                    console.log(f"[red]ModuleNotFoundError: {user_input[2]} couldn't be found..[/]");
            if user_input[1] == "uninstall":
                try:
                    subprocess.call(["py", "-m", "pip", "uninstall", f"{user_input[2]}"])
                except ModuleNotFoundError:
                    console.log(f"[red]ModuleNotFoundError: {user_input[2]} couldn't be found..[/]")
                    
        if user_input[0] == "pip" and root_access is False:
            console.log("[bold][yellow]You need [red]root[/] access to run this command!")
            continue


        if user_input[0] == "pylint":
            if os.path.exists(user_input[1]) and ".py" in user_input[1]:
                try:
                    os.system(f"pylint {user_input[1]}")
                except PermissionError:
                    try:
                        subprocess.call(["pylint", f"{user_input[1]}"])
                    except Exception:
                        console.log(f"[bold][red]Error: unable to run pylint on {user_input[1]}.[/]")  


        if user_input[0] == "code":
            if user_input[1] == ".":
                try:
                    os.system("code .") 
                except Exception:
                    try:
                        subprocess.call(["code", "."])
                    except Exception:
                        console.log("[bold][red]Error: unable to open VSCode.[/]")  
            if user_input[1] != ".":
                if os.path.exists(user_input[1]) and ".py" in user_input[1]:
                    try:
                        os.system(f"code {user_input[1]}")
                    except Exception:
                        try:
                            subprocess.call(["code", f"{user_input[1]}"])
                        except Exception:
                            console.log(f"[bold][red]Error: unable to open {user_input[1]} in VSCode.[/]")  
                if os.path.exists(user_input[1]) is False and ".py" in user_input[1]:
                    console.log(f"[bold][red]Error: Unable to open {user_input[1]} in VSCode as {user_input[1]} either isn't in the current working directory or it doesn't exist.[/]")

        
        if user_input[0] == "ls":
                try:
                    for items in os.listdir(user_input[1]):
                        print(f"[bold][yellow]{items}[/]")
                except IndexError:
                    for items in os.listdir(os.getcwd()):
                        print(f"[bold][yellow]{items}[/]")


        if user_input[0] == "mkdir":
            os.mkdir(user_input[1])
            console.print(f"[bold][yellow]Created {user_input[1]}[/]")


        if user_input[0] == "touch":
            try:
                user_input[1] = f"{user_input[1]}.txt" if "." not in f"{user_input[1]}[:-4]" else user_input[1]
                with open(user_input[1], "w") as file:
                    file.write("")
            except IndexError:
                console.log("[bold][red]No filename specified![/]")


        if user_input[0] == "cd":

            try:
                if user_input[2] == "-ls":
                    dir_ = user_input[1]

                    for items in os.listdir(dir_):
                        print(f"[bold][yellow]{items}[/]")

                    if os.path.exists(fr".\\{dir_}"):
                        os.chdir(dir_)
                        current_directory = fr"{current_directory}/{dir_}"
            except IndexError:

                if user_input[1] != "?origin":
                    dir_ = user_input[1]
                    if os.path.exists(fr".\\{dir_}"):
                        os.chdir(dir_)
                        current_directory = fr"{current_directory}/{dir_}"
                    if os.path.exists(fr".\\{dir_}"):
                        console.log(f"[bold]Couldn't find [yellow]{dir_}[/] in current directory.[/]")
                                 
                if user_input[1] == "?origin":
                    os.chdir(loop_back_directory)
                    current_directory = os.curdir


        if user_input[0] == "newthr":

            if user_input[1] == "pyflix":
                app_thread = Thread(target=pyflix, daemon=True)
                #subprocess.run(["cmd.exe", "/c", "start", "py", pyflix], timeout=15)
                app_thread.start()

            if user_input[1] == "youtube-dl":
                main = YoutubeDL()
                app_thread = Thread(target=main.run(console._input("[bold][yellow]Link: [/]")), daemon=True)
                #subprocess.run(["cmd.exe", "/c", "start", f"{app_thread}"], timeout=15)
                app_thread.start()

            if ".py" in user_input[1] and os.path.exists(user_input[1]):
                module = importlib.import_module(user_input[1])
                app_thread = Thread(target=module, daemon=True)
                app_thread.start()
                

        if user_input[0] == "systime":

            if user_input[1] in ("-e", "--edit"):
                check_time_settings(user_input[1])

            if user_input[1] in ("-v", "--view"):
                check_time_settings("-v")


        if user_input[0] == "open":


            if user_input[1] in ("-va", "--viewapps"):
                console.print("[bold][blue]Py[/][yellow]flix[/] -> Movie Viewer (use '[yellow]-o pyflix[/]' or '[yellow]--open pyflix[/]' to open pyflix) \n[red]Youtube-DL[/] -> Downloads Youtube Videos (use '[yellow]-o youtube-dl[/]' or '[yellow]--open youtube-dl[/]' to open Youtube-DL)\n[yellow]Py[/][blue]Vim[/] -> A cli based file editor")
                continue

            if user_input[1] in ("-a", "--all"):
                if "~" in current_directory:
                    dir_ = current_directory.replace("~", ".")
                for items in dir_:
                    print(items)
                    os.startfile(items)
                    if ".mp4" in items:
                        duration = 1
                        os.startfile(items)
                        time.sleep(duration)
                    else:
                        try:
                            with open(items, "r")as file:
                                contents = file.read()
                            console.print(f"[bold][yellow]{contents}[/]")
                        except PermissionError:
                            pass
            
            if user_input[1] == "pyvim":
                try:
                    if os.path.exists(user_input[2]) is True and ".py" in user_input[2]: 
                        os.system(f"pyvim {user_input[2]}")
                        os.system("cls")
                        continue
                    if user_input[2] in ("-c", "--credits"):
                        console.print("[bold][yellow]PyVim[/] was created by [yellow]Jonathan Slenders\nhttps://github.com/prompt-toolkit/pyvim[/]")
                except IndexError:
                    os.system("pyvim")
                    os.system("cls")
                    continue

            if user_input[1] in ("pyflix", "Pyflix"):
                pyflix()
                os.system("cls")
                continue

            if user_input[1] in ("youtube-dl", "Youtube-DL"):
                try:
                    main = YoutubeDL()
                    main.run(user_input[2])
                    os.system("cls")
                    continue
                except IndexError:
                    main = YoutubeDL()
                    main.run(input("[bold][yellow]Link: [/]"), 1)
                    os.system("cls")
                    continue

            if os.path.exists(user_input[1]):

                if os.path.exists(user_input[1]): # Bruh
                    with open(user_input[1], "r")as file:
                        contents = file.read()
                    console.print(f"[bold][yellow]{contents}[/]")

                if os.path.exists(user_input[1]) is False:
                    console.log(f"[bold][red]Error: {user_input[1]} either isn't in the current working directory or it doesn't exist.[/]")
            
            if ".mp4" in user_input[1]:
                os.startfile(user_input[1])
                console.log(f"[bold][yellow]Playing {user_input[1]} now..[/]")

            if os.path.exists(user_input[1]) is False and user_input[1] != "pyvim":
                    console.log(f"[bold][red]Error: {user_input[1]} either isn't in the current working directory or it doesn't exist.[/]")


        if user_input[0] in ("delete", "del"):
            os.remove(user_input[1])
            console.print(f"[bold][yellow]Deleted {user_input[1]}[/]")
            

        if user_input[0] == "exit":
            try:
                if user_input[1] == "root":
                    root_access: bool = False
                    os.system("cls")
            except IndexError:
                os.system("cls")
                sys.exit()

        if user_input[0] not in (command_list):
            console.log(f"[bold][red]'{user_input[0]}' is not a valid command![/]")

            
if __name__ == "__main__":
    PyiaShell()
