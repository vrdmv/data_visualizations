from random import randint

class Die():
    """A class representing a single die."""

    def __init__(self, sides=6):
        """Assume a six-sided die."""
        self.sides = sides

    def roll_the_dice(self):
        """Return a random value between 1 and the number of sides."""
        return randint(1,self.sides)

