from rich import *
commands = """[bold]Help command ([yellow]help[/]) -> Gets all available commands

Clear command ([yellow]clear[/] or [yellow]cls[/]) -> Clears the terminal screen

Open command ([yellow]open[/] [purple]{item}[/]) -> Opens an application [white]/[/] file (use [yellow]-va[/] or [yellow]--viewapps[/] to see available applications)
Delete command ([yellow]delete[/] [purple]{item}[/]) -> Can delete file or folder

Pip install command ([yellow]pip install[/] [purple]{module}[/]) -> Installs a python module that has been specified ([red]Needs root access[/])
Pip uninstall command ([yellow]pip uninstall[/] [purple]{module}[/]) -> Uninstalls a python module that has been specified ([red]Needs root access[/])

Root command ([red]root[/] or [red]root -e/--exit[/]) -> Establishes root access

Pylint command ([yellow]pylint[/] [purple]{python file}[/]) -> Rates your python file on it's readability

VSCode command ([yellow]code[/] [gray].[/] or [yellow]code[/] [purple]{python file}[/]) -> Opens VSCode if it is installed

Make Directory command ([yellow]mkdir[/] [purple]{name}[/]) -> Creates a folder with the name specified
listdir command ([yellow]ls [/][purple]{directory}[/] or [yellow]ls[/]) -> lists all items in directory or current directory
Change Directory command ([yellow]cd [/][purple]{directory}[/] or [yellow]cd [/][purple]{directory}[/] [yellow]-ls[/] or [yellow]cd ?origin[/]) -> changes current working directory (-ls option prints all items in the directory you are changing to) 

System Time command ([yellow]systime[/] [gray]-v / --view[/] or [yellow]systime[/] [gray]-e / --edit[/]) -> Changes the way date is formatted in the console 
New Thread command ([yellow]newthr [/][purple]{application}[/]) -> launches app in separate thread [red](NOTE: THIS IS BROKEN RIGHT NOW!)[/]

Exit command ([yellow]exit[/]) -> Exits PyiaShell (duh)
"""
