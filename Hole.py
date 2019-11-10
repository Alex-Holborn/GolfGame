class Hole:

    def __init__(self):
        self.number = 0
        self.distance = 0
        self.par = 0

    def set_par(self, par):
        self.par = par

    def set_distance(self, dist):
        self.distance = dist

    def set_number(self, number):
        self.number = number

    def __str__(self):
        return "Hole #{0} Par {1} Distance {2} Yards".format(self.number, self.par, self.distance)
