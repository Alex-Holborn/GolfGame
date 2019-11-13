class Course:

    def __init__(self):
        self.holes = []
        self.current_hole = 0
        self.shots_taken = 0
        print("Course Created.")

    def add_hole(self, hole):
        self.holes.append(hole)
        pass

    def get_hole_by_number(self, number):
        return self.holes[number - 1]

    def complete_hole(self):
        self.current_hole += 1

    def play_next_hole(self):
        self.holes[self.current_hole].play_hole()

    def play_course(self):
        print("Let's play golf!")
        self.play_next_hole()
