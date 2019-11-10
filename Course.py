class Course:

    def __init__(self):
        self.holes = []
        self.current_hole = 0
        print("Course Created.")

    def add_hole(self, hole):
        self.holes.append(hole)
        pass
