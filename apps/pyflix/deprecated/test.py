#import time
#animation = r"""|/-\"""
#idx = 0
#while True:
#    print(animation[idx % len(animation)], end="\r")
#    idx += 1
#   time.sleep(0.1)

#import time

#bar = [
#    " [=     ]",
#    " [ =    ]",
#    " [  =   ]",
#    " [   =  ]",
#    " [    = ]",
#    " [     =]",
#    " [    = ]",
#    " [   =  ]",
#    " [  =   ]",
#    " [ =    ]",
#]
#i = 0
#
#while True:
#    print(bar[i % len(bar)], end="\r")
#    time.sleep(.2)
#    i += 1

import time
from colorama import Fore
def rgbLoadingBar(speed):
    animation = [
    f"[        ]",
    f"[{Fore.LIGHTCYAN_EX}={Fore.RESET}       ]",
    f"[{Fore.CYAN}=={Fore.RESET}        ]",
    f"[{Fore.LIGHTBLUE_EX}==={Fore.RESET}      ]",
    f"[{Fore.BLUE}===={Fore.RESET}    ]",
    f"[{Fore.LIGHTMAGENTA_EX}====={Fore.RESET}   ]",
    f"[{Fore.MAGENTA}======{Fore.RESET}  ]",
    f"[{Fore.LIGHTYELLOW_EX}======={Fore.RESET} ]",
    f"[{Fore.YELLOW}========{Fore.RESET}]",
    f"[{Fore.LIGHTGREEN_EX} ======={Fore.RESET}]",
    f"[{Fore.GREEN}  ======{Fore.RESET}]",
    f"[{Fore.LIGHTRED_EX}   ====={Fore.RESET}]",
    f"[{Fore.RED}    ===={Fore.RESET}]",
    f"[{Fore.LIGHTCYAN_EX}     ==={Fore.RESET}]",
    f"[{Fore.CYAN}      =={Fore.RESET}]",
    f"[{Fore.LIGHTMAGENTA_EX}       ={Fore.RESET}]",
    f"[        ]"
    ]

    notcomplete = True

    i = 0

    while notcomplete:
        print(animation[i % len(animation)], end='\r')
        time.sleep(speed)
        i += 1
""" 
frame1 = f"         {Fore.MAGENTA}o{Fore.RESET} {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}!"
frame2 = f"        {Fore.MAGENTA}t{Fore.RESET}{Fore.YELLOW}o {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}!"
frame3 = f"     {Fore.MAGENTA}e{Fore.RESET} {Fore.YELLOW}t{Fore.RESET}{Fore.BLUE}o{Fore.RESET} {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}!" 
frame4 = f"     {Fore.MAGENTA}m{Fore.RESET}{Fore.YELLOW}e{Fore.RESET} {Fore.BLUE}t{Fore.RESET}{Fore.CYAN}o{Fore.RESET} {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}!"
frame5 = f"    {Fore.MAGENTA}o{Fore.RESET}{Fore.YELLOW}m{Fore.RESET}{Fore.BLUE}e{Fore.RESET} {Fore.CYAN}t{Fore.RESET}{Fore.GREEN}o{Fore.RESET} {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}!"
frame6 = f"   {Fore.MAGENTA}c{Fore.RESET}{Fore.YELLOW}o{Fore.RESET}{Fore.BLUE}m{Fore.RESET}{Fore.CYAN}e{Fore.RESET} {Fore.GREEN}t{Fore.RESET}o {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}!"
frame7 = f"  lcome to {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}!"
frame8 = f" elcome to {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}!"
frame9 = f"Welcome to {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}!"
frame10 = f"Welcome to {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}!"
"""
rgbLoadingBar(0.5)