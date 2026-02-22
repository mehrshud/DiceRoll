# Tech stack fixed to Python
from random import randint

class DiceRoll:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)