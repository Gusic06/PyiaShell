"""This one does work, I think"""
from pytube import YouTube
from rich import *
from rich.console import *
from rich.progress import *
import time

def youtubeDl(link):

    yt = YouTube(link)
    console = Console()

    console.print(f"\n[bold][yellow]Title:[/] {yt.title}")
    console.print(f"[bold][yellow]Views:[/] {yt.views}")

    userInput: str = console.input("\n[bold][yellow]Is this the video you want to download?[/] (Y/N) -> ").title()

    if userInput == "Y" or userInput == "Yes":

        videoDownload = yt.streams.get_highest_resolution()
        console.print(f"[bold]Downloading [yellow]{yt.title}[/] now.")
        videoDownload.download()

        if userInput == "N" or userInput == "No":
            pass

if __name__ == "__main__":
    console = Console()
    youtubeDl(console.input("[bold][yellow]Link: [/]"))
