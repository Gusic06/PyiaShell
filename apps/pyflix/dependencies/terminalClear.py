#!/usr/bin/env python
import os
import sys
import time
import platform
import subprocess
def terminalClear(seconds: float):
    """
    Accepts either an integer or a floating point value for the 'seconds' parameter.
    """
    if not isinstance(seconds, float):
        if isinstance(seconds, int):
            seconds = seconds + .0 #Turning int into a float so the function can work without raising an exception
            seconds = float(seconds)
            time.sleep(seconds)
            os.system("cls")
            #os.system("clear")
        else:
            raise TypeError(f"Expected {float} or {int} but got {type(seconds)} instead.")
    else:
        time.sleep(seconds)
        os.system("cls")
if __name__ == "__main__":
    terminalClear(1)