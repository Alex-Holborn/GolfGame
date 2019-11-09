import CourseCreator

class Game:

    def __init__(self):
        self.number_of_players = self.get_number_of_players()
        if self.number_of_players == 1:
            self.is_single_player = True
        else:
            self.is_single_player = False
        self.player_names = self.get_player_names()
        print(self.number_of_players)
        print(self.player_names)
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
        print(choice)

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


Game()
