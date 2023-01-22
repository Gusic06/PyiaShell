"""Source file for PyiaShell"""
from rich.console import Console
from rich import *
from rich.panel import Panel
from rich.traceback import install
from rich.tree import Tree

from os import curdir, getcwd, getlogin, system, mkdir, listdir, startfile, remove, chdir
from os.path import exists
from subprocess import call
from sys import exit as sys_exit

from time import strftime, sleep
from threading import Thread
import importlib
from pathlib import Path
from getpass import getpass
from cryptography.fernet import Fernet
import re as regex

from apps.pyflix.pyflix import pyflix
from apps.youtube_dl.youtube import YoutubeDL
from apps.youtube_dl.youtube_dl import youtubeDl
from dependencies.commands import commands
from dependencies.check_time_settings import check_time_settings
from dependencies.command_list import command_list
from dependencies.dir_tree import walk_directory


def PyiaShell():

    install()
    console = Console(color_system="truecolor")

    OSNAME = getlogin()

    system("cls")

    console.print(Panel("[bold][yellow]Welcome![/]\n\nUse [yellow]help[/] to learn what commands are available.[/]", title_align="center", title="[bold][blue]Py[/][yellow]thonia[/]", border_style=""))
    current_directory = curdir
    loop_back_directory = getcwd()
    root_file_directory = f"{curdir}\\root\\password.txt"
    root_access: bool = False

    while True:

        time_setting = check_time_settings("-") # Giving the function a none value to get an output

        current_date = strftime("%d/%m/%y") if time_setting == "EU" else strftime("%m/%d/%y")
        current_directory = '~' if current_directory == "." else current_directory
        
        if root_access is True:
            console.print(f"\n[bold][red]root@{OSNAME} | {current_directory} | [{current_date}][/]")
            user_input = console.input("[bold][red]> [/]")
        if root_access is False:
            console.print(f"\n[bold][green]pyia@{OSNAME} | [yellow]{current_directory}[/] | [{current_date}][/]")
            user_input = console.input("[bold]> [/]")
        
        user_input = user_input.split(" ", 4)
        
        
        if user_input[0] == "run":
            if ".py" in user_input[1] and exists(user_input[1]):
                try:
                    system(f"py {user_input[1]}")
                except Exception:
                    try:
                        call(["py", f"{user_input[1]}"])
                    except:
                        console.log("[bold][red]Err[/]")

        
        if user_input[0] == "help":
            console.print(f"\n{commands}")


        if user_input[0] in ("clear", "cls"):
            system("cls")

        
        if user_input[0] == "root":
            _dir = current_directory.replace("~", ".") # Temporarily storing the current directory in a variable so it can be used later
            chdir(loop_back_directory)
                
            try:
                if user_input[1] in ("-e", "--exit") and root_access is True:
                    root_access: bool = False
                    system("cls")
                    chdir(loop_back_directory)
                    chdir(_dir)
                    continue
                if user_input[1] in ("-e", "--exit") and root_access is False:
                    console.log("[bold][red]You don't have root access![/]")
                    chdir(loop_back_directory)
                    chdir(_dir)
                    continue
                if user_input[1] not in ("-e", "--exit") and root_access is True:
                    console.log("[bold][red]You already have root access![/]")
                    chdir(loop_back_directory)
                    chdir(_dir)
                    continue
            except IndexError:
                if root_access is True:
                    console.log("[bold][red]You already have root access![/]")
                    chdir(loop_back_directory)
                    chdir(_dir)
                    continue
                else:
                    chdir(loop_back_directory)
                    chdir(_dir)
                    pass

            if exists(fr"{loop_back_directory}\\root") is False:
                system("cls")

                console.print("[bold][red]A root password has not been set yet.[/]")
                console.print("[bold][red]Please set a password.[/]", highlight=True)
                console.print("[bold][red]> [/]", end="")
                root_password = getpass("")

                mkdir("root")

                if exists(fr"{loop_back_directory}\\key\\KEY.key") is False:
                    KEY = Fernet.generate_key()
                    mkdir("key")
                    with open(fr"{loop_back_directory}\\key\\KEY.key", "wb") as file:
                        file.write(KEY)
                    
                with open(fr"{loop_back_directory}\\key\\KEY.key", "rb") as file:
                    _key = file.read()
                KEY = Fernet(_key)

                root_password = KEY.encrypt(bytes(root_password, "utf-8"))

                with open(fr"{loop_back_directory}\\root\\password.txt", "w") as file:
                    file.write(root_password)

                chdir(loop_back_directory)
                chdir(_dir)
                system("cls")

            if exists(fr"{loop_back_directory}\\root\\password.txt"):

                system("cls")

                console.print("[bold][red]Please enter your password.[/]")
                console.print("[bold][red]> [/]", end="")
                root_password = getpass("")

                if exists(fr"{loop_back_directory}\\key\\KEY.key") is False:
                    KEY = Fernet.generate_key()
                    mkdir("key")
                    with open(fr"{loop_back_directory}\\key\\KEY.key", "wb") as file:
                        file.write(KEY)
                if exists(fr"{loop_back_directory}\\key\\KEY.key"):
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
                    system("cls")

                    console.print("[bold][red]Incorrect password![/]")
                    sleep(1.5)

                chdir(loop_back_directory)
                chdir(_dir)
                system("cls")


        if user_input[0] == "pyvim":

            try:
                if exists(user_input[1]) and ".py" in user_input[1]:
                    try:
                        system(f"pyvim {user_input[1]}")
                    except PermissionError:
                        try:
                            call(["pyvim", user_input[1]])
                        except PermissionError:
                            console.log(f"[bold][red]PermissionError: Unable to open {user_input[1]}[/]")
            except IndexError:
               try:
                   system("pyvim")
               except PermissionError:
                   try:
                       call(["pyvim"])
                   except PermissionError:
                       console.log("[bold][red]PermissionError: Unable to open pyvim[/]")


        if user_input[0] in ("youtube-dl", "Youtube-DL"):
            try:
                system("cls")
                main = YoutubeDL()
                try:
                    youtubeDl(user_input[1])
                except IndexError:
                    youtubeDl(console.input("[bold][yellow]Link: [/]"))
                system("cls")
            except Exception:
                pass


        if user_input[0] == "pip" and root_access is True:

            if user_input[1] == "install":
                try:
                    call(["py", "-m", "pip", "install", f"{user_input[2]}"])
                except ModuleNotFoundError:
                    console.log(f"[red]ModuleNotFoundError: {user_input[2]} couldn't be found..[/]");
            if user_input[1] == "uninstall":
                try:
                    call(["py", "-m", "pip", "uninstall", f"{user_input[2]}"])
                except ModuleNotFoundError:
                    console.log(f"[red]ModuleNotFoundError: {user_input[2]} couldn't be found..[/]")
                    
        if user_input[0] == "pip" and root_access is False:
            console.log("[bold][yellow]You need [red]root[/] access to run this command!")
            continue


        if user_input[0] == "pylint":
            if exists(user_input[1]) and ".py" in user_input[1]:
                try:
                    system(f"pylint {user_input[1]}")
                except PermissionError:
                    try:
                        call(["pylint", f"{user_input[1]}"])
                    except Exception:
                        console.log(f"[bold][red]Error: unable to run pylint on {user_input[1]}.[/]")  


        if user_input[0] == "code":
            if user_input[1] == ".":
                try:
                    system("code .") 
                except Exception:
                    try:
                        call(["code", "."])
                    except Exception:
                        console.log("[bold][red]Error: unable to open VSCode.[/]")  
            if user_input[1] != ".":
                if exists(user_input[1]) and ".py" in user_input[1]:
                    try:
                        system(f"code {user_input[1]}")
                    except Exception:
                        try:
                            call(["code", f"{user_input[1]}"])
                        except Exception:
                            console.log(f"[bold][red]Error: unable to open {user_input[1]} in VSCode.[/]")  
                if exists(user_input[1]) is False and ".py" in user_input[1]:
                    console.log(f"[bold][red]Error: Unable to open {user_input[1]} in VSCode as {user_input[1]} either isn't in the current working directory or it doesn't exist.[/]")

        
        if user_input[0] == "ls":
                try:

                    if user_input[2] in ("-t", "--tree"):
                        directory = user_input[1]
                        tree = Tree(
                            f":open_file_folder: [link file://{directory}]{directory}",
                            guide_style="bold bright_blue",
                        )
                        walk_directory(Path(directory), tree)
                        print(tree)

                    if user_input[1] in ("-t", "--tree"):
                        directory = curdir
                        tree = Tree(
                            f":open_file_folder: [link file://{directory}]{directory}",
                            guide_style="bold bright_blue",
                        )
                        walk_directory(Path(directory), tree)
                        print(tree)

                    if user_input[1] not in ("-t", "--tree") and user_input[2] not in ("-t", "--tree"):
                        for items in listdir(user_input[1]):
                            print(f"[bold][yellow]{items}[/]")

                except IndexError:
                    for items in listdir(getcwd()):
                        print(f"[bold][yellow]{items}[/]")


        if user_input[0] == "mkdir":
            mkdir(user_input[1])
            console.print(f"[bold][yellow]Created {user_input[1]}[/]")


        if user_input[0] == "touch":
            try:
                try:
                    if user_input[2] == ">>":
                        _string = " ".join(user_input)
                        find_contents = regex.search('"', _string)
                        index_of_string = find_contents.span()
                        file_contents = _string[index_of_string[1]:-1:1] # Slicing from the start of the string to the end of the string to get the contents
                        with open(user_input[1], "w") as file:
                            file.write(file_contents)
                except IndexError:
                    user_input[1] == f"{user_input[1]}.txt" if "." not in f"{user_input[1]}[:4]" else user_input[1]
                    with open(user_input[1], "w") as file:
                        file.write("")
            except IndexError:
                console.log("[bold][red]No filename specified![/]")


        if user_input[0] == "cd":

            try:
                if user_input[2] == "-ls":
                    dir_ = user_input[1]

                    for items in listdir(dir_):
                        print(f"[bold][yellow]{items}[/]")

                    if exists(fr".\\{dir_}"):
                        chdir(dir_)
                        past_directory = current_directory
                        current_directory = fr"{current_directory}/{dir_}"
                        
            except IndexError:

                if user_input[1] != "?origin":
                    dir_ = user_input[1]
                    if dir_ == "..":
                        try:
                            chdir(past_directory)
                            current_directory = fr"{past_directory}/{current_directory}"
                        except Exception as Err:
                            console.log(f"[bold]Couldn't move up the directory tree -> {Err}[/]")
                    if exists(fr".\\{dir_}") is False:
                        console.log(f"[bold]Couldn't find [yellow]{dir_}[/] in current directory.[/]")
                        pass
                    if exists(fr".\\{dir_}"):
                        chdir(dir_)
                        current_directory = fr"{current_directory}/{dir_}"
                                 
                if user_input[1] == "?origin":
                    chdir(loop_back_directory)
                    current_directory = curdir


        if user_input[0] == "newthr":

            if user_input[1] == "pyflix":
                app_thread = Thread(target=pyflix, daemon=True)
                #run(["cmd.exe", "/c", "start", "py", pyflix], timeout=15)
                app_thread.start()

            if user_input[1] == "youtube-dl":
                main = YoutubeDL()
                app_thread = Thread(target=main.run(console._input("[bold][yellow]Link: [/]")), daemon=True)
                #run(["cmd.exe", "/c", "start", f"{app_thread}"], timeout=15)
                app_thread.start()

            if ".py" in user_input[1] and exists(user_input[1]):
                module = importlib.import_module(user_input[1])
                app_thread = Thread(target=module, daemon=True)
                app_thread.start()
                

        if user_input[0] == "systime":

            if user_input[1] == "-e" or user_input[1] == "--edit":
                check_time_settings(user_input[1])

            if user_input[1] == "-v" or user_input[1] == "--view":
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
                    startfile(items)
                    if ".mp4" in items:
                        duration = 1
                        startfile(items)
                        sleep(duration)
                    else:
                        try:
                            with open(items, "r")as file:
                                contents = file.read()
                            console.print(f"[bold][yellow]'{items}' >> {contents}[/]")
                        except PermissionError:
                            pass
            
            if user_input[1] == "pyvim":
                try:
                    if exists(user_input[2]) is True and ".py" in user_input[2]: 
                        system(f"pyvim {user_input[2]}")
                        system("cls")
                        continue
                    if user_input[2] in ("-c", "--credits"):
                        console.print("[bold][yellow]PyVim[/] was created by [yellow]Jonathan Slenders\nhttps://github.com/prompt-toolkit/pyvim[/]")
                except IndexError:
                    system("pyvim")
                    system("cls")
                    continue

            if user_input[1] in ("pyflix", "Pyflix"):
                pyflix()
                system("cls")
                continue

            if user_input[1] in ("youtube-dl", "Youtube-DL"):
                try:
                    main = YoutubeDL()
                    main.run(user_input[2])
                    system("cls")
                    continue
                except IndexError:
                    main = YoutubeDL()
                    main.run(input("[bold][yellow]Link: [/]"), 1)
                    system("cls")
                    continue

            if exists(user_input[1]): # Some spaghetti code garbage

                if exists(user_input[1]):
                    with open(user_input[1], "r")as file:
                        contents = file.read()
                    console.print(f"[bold][purple]{user_input[1]} >>[/] [yellow]'{contents}'[/]")

                if exists(user_input[1]) is False:
                    console.log(f"[bold][red]Error: {user_input[1]} either isn't in the current working directory or it doesn't exist.[/]")
            
            if ".mp4" in user_input[1]:
                try:
                    startfile(user_input[1])
                    console.log(f"[bold][yellow]Playing {user_input[1]} now..[/]")
                except FileNotFoundError:
                    console.log(f"[bold][red]Couldn't find {user_input[1]} in current directory[/]")

            if exists(user_input[1]) is False and user_input[1] != "pyvim":
                    console.log(f"[bold][red]Error: {user_input[1]} either isn't in the current working directory or it doesn't exist.[/]")


        if user_input[0] in ("delete", "del"):
            try:
                remove(user_input[1])
                console.print(f"[bold][yellow]Deleted {user_input[1]}[/]")
            except Exception as Err:
                console.log(f"[bold][purple]Unable to delete {user_input[1]} >> [yellow]{Err}[/]")
                continue # We need this otherwise it bugs out
            

        if user_input[0] == "exit":
            try:
                if user_input[1] in ("root"):
                    root_access: bool = False
                    system("cls")
            except IndexError:
                system("cls")
                sys_exit()

        if user_input[0] not in command_list:
            console.log(f"[bold][red]'{user_input[0]}' is not a valid command![/]")


if __name__ == "__main__":
    PyiaShell()
    
