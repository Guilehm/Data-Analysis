from random import randint

class Die():
    """ a class that represents a single dice """

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """ show a random value of sides """
        return randint(1, self.num_sides)
