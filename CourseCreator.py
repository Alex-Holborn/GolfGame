import Course
import HoleCreator
import random

class CourseCreator:

    def __init__(self, is_full_round):
        if is_full_round:
            print("Creating Full Course...")
        else:
            print("Creating Half Course...")
        hole_sizes = self.calculate_hole_sizes(is_full_round)
        #print(hole_sizes)
        #print(self.total_par(hole_sizes))
        self.course = Course.Course()
        for i in enumerate(hole_sizes):
            hc = HoleCreator.HoleCreator(self.course, i[0] + 1, i[1])
            self.course.add_hole(hc.hole)
        #for hole in self.course.holes:
            #print(hole)

    def calculate_hole_sizes(self, is_full_round):
        hole_sizes = []
        holes = 18
        if not is_full_round:
            holes = 9
        for i in range(0, holes):
            r = random.randint(0, 100)
            if r < 20:
                hole_sizes.append(3)
            elif r < 45:
                hole_sizes.append(5)
            else:
                hole_sizes.append(4)
        return hole_sizes

    def total_par(self, hole_sizes):
        total = 0
        for i in hole_sizes:
            total += i
        return total
