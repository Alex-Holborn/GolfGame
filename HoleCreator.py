import Hole
import random

class HoleCreator:

    def __init__(self, course, number, par):
        self.hole = Hole.Hole(course)
        self.hole.set_number(number)
        self.hole.set_par(par)
        self.hole.set_distance(self.create_distance(par))
        self.hole.reset_distance_left()

    def get_hole(self):
        return self.hole

    def create_distance(self, par):
        if par == 3:
            return random.randint(220, 255)
        if par == 4:
            return random.randint(260, 450)
        if par == 5:
            return random.randint(455, 690)
