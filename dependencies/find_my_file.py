"""Function for PyiaShell"""
from glob import glob
from os import curdir
from os.path import splitext
from shutil import copy
import pathlib
def find_my_file(file) -> str:
    """Takes one input which is file (Note: {file} should have a file extension to make this function work properly)"""
    directory = glob(fr"{pathlib.Path.home().drive}\\**\\*{(splitext(file))[1]}") #pathlib.Path.home().drive is the drive letter and (splitext(file))[1] is the file extension
    for _dir in directory:
        if file in _dir:
            print(f"Successfully found '{file}' in '{_dir}'")
            user_input = input(f"Do you want to copy '{file}' to the current directory? (Y/N) -> ").title()
            if user_input in ("Yes", "Y"):
                copy(_dir, f"{curdir}\\{file}")
                print(f"Successfully copied '{file}' to the current directory")
            if user_input in ("No", "N"):
                pass
            return _dir
    else:
        print(f"'{file}' couldn't be found..")
if __name__ == "__main__":
    find_my_file("test.txt")
