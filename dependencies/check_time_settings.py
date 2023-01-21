import time
import os
from rich.console import *
from rich import *
from rich.traceback import *
def check_time_settings(_input: str):
    
    console = Console()
    global time_setting

    if _input == "-":
        try:
            if "US" in time_setting:
                time_setting = "US"
                return time_setting

            if "EU" in time_setting:
                time_setting = "EU"
                return time_setting

        except NameError:
            time_setting = "EU"
            return time_setting

    if _input in ("-v", "--view"):

        if "US" in time_setting:
            time_setting = "US"
            console.print(f"[bold]Current time layout: [yellow]{time_setting}[/]")
            return time_setting

        if "EU" in time_setting:
            time_setting = "EU"
            console.print(f"[bold]Current time layout: [yellow]{time_setting}[/]")
            return time_setting

    if _input in ("-e", "--edit"):
        
        user_input = console.input("[bold][yellow]Select time layout\n1) Day/Month/Year\nor\n2) Month/Day/Year[/]\n\n> ")

        if user_input == "1":
            time_setting = "EU"
            return time_setting

        if user_input == "2":
            time_setting = "US"
            return time_setting

        else:
            console.print("[bold][red]Err[/]")
if __name__ == "__main__":
    check_time_settings(input("-"))