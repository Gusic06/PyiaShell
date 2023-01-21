import glob
import os
def findFile(file):
    directory = glob.glob(r"C:\\**\\*")
    for items in directory:
        if file in items:
            print(items)
            return contents
if __name__ == "__main__":
    findFile("stare.mp4")

directory = glob.glob(r"C:\\**\\*")
for items in directory:
    if file in items:
        print(items)