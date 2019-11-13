class Hole:

    def __init__(self, course):
        self.course = course
        self.number = 0
        self.distance = 0
        self.par = 0
        self.has_been_played = False
        self.shots_taken = 0

    def set_par(self, par):
        self.par = par

    def set_distance(self, dist):
        self.distance = dist

    def set_number(self, number):
        self.number = number

    def play_hole(self):
        print(self)

    def __str__(self):
        return "Hole #{0} Par {1} Distance {2} Yards".format(self.number, self.par, self.distance)
