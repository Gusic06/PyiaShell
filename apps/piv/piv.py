"""I have no idea tbh"""
import os
import sys
import pygame
def piv():
    pivLoop: bool = True
    lineNumber = 0
    pygame.init()
    os.system("cls")
    while pivLoop is True:
        lineNumber += 1
        lineInput = input(f"{lineNumber}   | >  ")
        for i in range(1, 9823018):
            lineNumber += 1
            if lineNumber >= 10:
                lineInput = input(f"{lineNumber}  | >  ")
            else:
                lineInput = input(f"{lineNumber}   | >  ")
            for event in pygame.event.get():
                if event == pygame.K_TAB:
                    whitespace = sys.stdin.readline()
                    whitespace = len(whitespace)
                    for i in whitespace:
                        lineLength = " \r"
                    print(lineLength)
                    print("    \r")
                if event == pygame.K_LEFTBRACKET and event == pygame.K_LCTRL:
                    whitespace = sys.stdin.readline()
                    whitespace = len(whitespace)
                    for i in whitespace:
                        lineLength = " \r"
                    print(lineLength)
                    print(f"{lineLength})")
            lines = sys.stdin.readlines()
            print(lines)
            lines = [line.splitlines() for line in sys.stdin]
            print(lines)
            exec(lines)
if __name__ == "__main__":
    piv()