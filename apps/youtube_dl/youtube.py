"""This one doesn't work just yet"""
import os
import sys
import subprocess
from pytube import YouTube

class YoutubeDL:

    """
A Simple Youtube Downloader,
    \nDownload Mode 1 -> Batch Download (From a Playlist) 
    \nDownload Mode 2 -> Single Download
    """


    def __init__(self):
        self.path = r".\\Downloaded Videos"


    def get_download_mode(self):
        print("1. | Batch Download (from playlist)\n2. | Single Download")
        self.download_choice = input("What mode do you want to select? -> ").upper()
        if self.download_choice in ("BATCH", 1):
            return "BATCH"
        if self.batch_download in ("SINGLE", 2):
            return "SINGLE"

        
    def download(self, link: str):
        self.yt = YouTube(link)
        print(f"Title: {self.yt.title}\nViews: {self.yt.views}")
        self.confirmation = input("Is this the correct video? (Y/N) -> ").title()
        if self.confirmation in ("Y", "Yes"):
            self.video = self.yt.streams.get_highest_resolution()
            self.video.download()
        if self.confirmation in ("N", "No"):
            pass


    def batch_download(self):
        if os.path.exists("playlist.txt"):
            with open("playlist.txt", "r") as file:
                self.playlist = file.read()
            if not isinstance(self.playlist, list):
                raise TypeError(f"Expected a {list} input but got {type(self.playlist)} instead.")
            for self.video in self.playlist:
                self.yt = YouTube(self.video)
                self.video_from_playlist = self.yt.streams.get_highest_resolution()
                self.video_from_playlist.download()
                print(f"Successfully downloaded {self.yt.title}!")
            else:
                print(f"Successfully downloaded all {len(self.playlist)} videos!")
        if os.path.exists("playlist.txt") is False:
            print("Unable to download from playlist.txt!")


    """
    def get_playlist_items(self):
        if os.path.exists("playlist.txt"):
            try:
                os.remove("playlist.txt")
            except PermissionError:
                raise PermissionError("Unable to delete 'playlist.txt'!")
        if os.path.exists("playlist.txt") is False:
            for self.item in playlist:
                with open("playlist.txt", "w") as file:
                    file.write(f"{self.item}\n")
            with open("playlist.txt", "r") as file:
                self.playlist = list(file.read())
            print(f"Successfully added {len(playlist)} number of links to playlist file")
    """

    def check_download_path(self):
        if os.path.exists(self.path):
            pass
        if os.path.exists(self.path) is False:
            try:
                os.mkdir("Downloaded Videos")
            except PermissionError:
                try:
                    print("Failed to create 'Downloaded Videos' folder.\nAttempting to create folder again, please wait.")
                    subprocess.call(["mkdir", "Downloaded Videos"])
                except PermissionError:
                    print("Err")
                    sys.exit()


    def run(self):
        self.check_download_path()
        self.mode = self.get_download_mode()
        if self.mode == "SINGLE":
            self.download(input("Link: "))
        if self.mode == "BATCH":
            self.playlist_generator = CreatePlaylist()
            self.playlist_generator.run()
            self.batch_download()


class CreatePlaylist(YoutubeDL):

    def get_links_from_user(self):
        self.loop: bool = True
        self.playlist: list = []
        print("Add links to playlist.\nInput 'exit' to escape from the loop")
        while self.loop is True:
            self.link: str = input("Link: ")
            if self.link not in "exit":
                self.playlist.append[self.link]
            if self.link in "exit":
                self.loop: bool = False
        print(f"Successfully added {len(self.playlist)} number of links to playlist file")
        return self.playlist

    def generate_playlist_text_file(self):
        print("Generating playlist file..")
        with open("playlist.txt", "w") as file:
            file.write(self.playlist)
        print("Done!")

    def run(self):
        self.get_links_from_user()
        self.generate_playlist_text_file()


if __name__ == "__main__":
    main = YoutubeDL()
    main.run()