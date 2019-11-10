import CourseCreator

class Game:

    def __init__(self):
        self.courses_played = []
        self.current_course = ""
        self.number_of_players = self.get_number_of_players()
        if self.number_of_players == 1:
            self.is_single_player = True
        else:
            self.is_single_player = False
        self.player_names = self.get_player_names()
        self.create_menu()

    def create_menu(self):
        options = ["p", "i", "q"]
        print("(P)lay a round of golf.")
        print("(I)nstructions.")
        print("(Q)uit.")
        choice = input("Make a selection: ")
        while choice.lower() not in options:
            choice = input("Make a valid selection: ")
        self.menu_choice(choice.lower())

    def menu_choice(self, choice):
        if choice == "p":
            self.play()
        elif choice == "i":
            self.print_instructions()
        elif choice == "q":
            print("Thanks for playing!")
            exit()

    def play(self):
        options = ["f", "h"]
        option = input("Play a (F)ull round or a (H)alf round?")
        while option.lower() not in options:
            option = input("Make a valid selection: (F)ull or (H)alf")
        if option.lower() == "f":
            self.current_course = self.create_course(True)
        else:
            self.current_course = self.create_course(False)

    def create_course(self, is_full_round):
        return CourseCreator.CourseCreator(is_full_round).course

    def print_instructions(self):
        print("Add instructions Martin")
        print("------------------------")
        self.create_menu()

    def get_player_names(self):
        if self.is_single_player:
            return input("Please enter your name: ")
        names = []
        for i in range(0, self.number_of_players):
            names.append(input("Player {0} please enter your name: ".format(i + 1)))
        return names

    def get_number_of_players(self):
        x = ""
        while type(x) != int:
            try:
                x = int(input("Please enter number of players: "))
            except ValueError:
                print("Please enter a valid number")
        return x

    def start_round(self):
        pass

Game()
