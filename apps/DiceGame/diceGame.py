"""Works fine"""
import random
import time
import sys
import keyboard

class DiceGame:

    def __init__(self, dice1, dice2):
        self.dice1 = dice1
        self.dice2 = dice2

    def rollDice(self):
        return random.randint(1, 6)
        
    def outputThrow(self):
        self.dice1: int = 0
        self.dice2: int = 0
        while self.dice1 == self.dice2:
            self.dice1: str = str(self.rollDice())
            self.dice2: str = str(self.rollDice())
        print(f"Dice 1: {self.dice1}\nDice 2: {self.dice2}")

if __name__ == "__main__":
    while not keyboard.is_pressed("esc"):
        main = DiceGame(0, 0)
        main.outputThrow()
        time.sleep(3)
        print("-" * 50)
        if keyboard.is_pressed("esc"):
            sys.exit()
