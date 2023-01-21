import random
import time
from terminalClear import terminalClear
from divider import divider

def rockPaperScissors(StartTime: int, EndTime: int):

    if not isinstance(StartTime, int):
        raise TypeError(f"Invalid param: Expected {int} but got {type(StartTime)} instead.")

    if not isinstance(EndTime, int):
        raise TypeError(f"Invalid param: Expected {int} but got {type(EndTime)} instead.")

    gameList = ["Rock", "Paper", "Scissors"]

    for i in range(StartTime, EndTime):

        terminalClear(0.5)

        print("Do you want to pick either:")
        divider()
        print(" ->  Rock\n ->  Paper\n ->  Scizzors")
        divider()
        userChoice = input("\nWhat do you want to choose? -> ").title()

        if userChoice == "Scizzors":
            userChoice: str = "Scissors"

        time.sleep(0.5)

        if not isinstance(userChoice, str):
            raise TypeError(f"Incorrect input: Expected {str} but got {type(userChoice)} instead.")

        aiChoice = random.choice(gameList)

        if userChoice == aiChoice:
            terminalClear(0.25)
            print(f"Round Tied:\nBoth you and the computer chose '{aiChoice}'.")
            time.sleep(0.5)

        if userChoice == "Rock" and aiChoice == "Scissors":
            terminalClear(0.25)
            print(f"You won that round:\nYou chose {userChoice}.\nThe computer chose {aiChoice}.")
            time.sleep(0.5)

        if userChoice == "Rock" and aiChoice == "Paper":
            terminalClear(0.25)
            print(f"You lost that round:\nYou chose {userChoice}\nThe computer chose {aiChoice}.")
            time.sleep(0.5)
        
        if userChoice == "Scissors" and aiChoice == "Paper":
            terminalClear(0.25)
            print(f"You won that round:\nYou chose {userChoice}.\nThe computer chose {aiChoice}.")
            time.sleep(0.5)
        
        if userChoice == "Scissors" and aiChoice == "Rock":
            terminalClear(0.25)
            print(f"You lost that round:\nYou chose {userChoice}\nThe computer chose {aiChoice}.")
            time.sleep(0.5)

        if userChoice == "Paper" and aiChoice == "Rock":
            terminalClear(0.25)
            print(f"You won that round:\nYou chose {userChoice}.\nThe computer chose {aiChoice}.")
            time.sleep(0.5)
        
        if userChoice == "Paper" and aiChoice == "Scissors":
            terminalClear(0.25)
            print(f"You lost that round:\nYou chose {userChoice}\nThe computer chose {aiChoice}.")
            time.sleep(0.5)

if __name__ == "__main__":
    rockPaperScissors(1, 10)