class Hole:

    def __init__(self, course):
        self.course = course
        self.number = 0
        self.distance = 0 #Total Distance of hole
        self.par = 0
        self.has_been_played = False
        self.shots_taken = 0
        self.distance_left = 0 #Total dynamic distance left to play
        self.current_club = 0

    def set_par(self, par):
        self.par = par

    def set_distance(self, dist):
        self.distance = dist

    def set_number(self, number):
        self.number = number

    def reset_distance_left(self):
        self.distance_left = self.distance

    def play_hole(self):
        print(self)
        self.distance_left = self.distance
        while self.distance_left > 0:
            self.take_next_shot()

    def take_next_shot(self):
        print("Shot #{0}. {1} Yards left to play.".format(self.shots_taken + 1, self.distance_left))
        print("Current club: ", self.get_club())
        choices = ["c", "s", "q"]
        choice = ""
        while choice not in choices:
            choice = input(" (S)wing\n (C)hange Club\n (Q)uit\n Please make a selection.").lower()
        if choice == "c":
            self.change_club()
        elif choice == "s":
            self.swing()
        else:
            self.course.exit()

    def swing(self):
        pass

    def change_club(self):
        choice = input("Enter number of club to select or \"L\" for list of clubs available.")
        try:
            x = int(choice)
            if 0 < x <= len(self.get_club_list()):
                self.set_club(x - 1)
            else:
                print("Please enter a valid number.")
                self.change_club()
        except ValueError:
            if choice.lower() == "l":
                self.print_club_list()
                self.change_club()
            else:
                print("Please make a valid selection.")
                self.change_club()

    def print_club_list(self):
        for e, i in enumerate(self.get_club_list()):
            print("{0}. {1}".format(e + 1, i))

    def get_club_list(self):
        return ["Driver", "3 Wood", "5 Wood", "3 Iron", "4 Iron", "5 Iron", "6 Iron", "7 Iron", "8 Iron", "9 Iron", "Pitching Wedge", "Putter"]

    def set_club(self, i):
        self.current_club = i

    def get_club(self):
        return self.get_club_list()[self.current_club]

    def __str__(self):
        return "Hole #{0} Par {1} Distance {2} Yards".format(self.number, self.par, self.distance)
