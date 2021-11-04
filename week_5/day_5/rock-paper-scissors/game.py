
import random

class Game():
    def __init__(self):
        pass


    def get_user_item(self):
        while True:
            user_choice_input = input("Please enter your choice:\nr - rock\np - paper\ns - scissors:\ne - exit\n")
            user_choice = user_choice_input.strip().lower()
            if user_choice  in ['r','s','p']:
                return user_choice
            if user_choice == 'e':
                return 'exit'

    def get_computer_item(self):
        comp_choice = random.choice(['r','s','p'])
        return comp_choice

    user_victories = [('r','s'),('p','r'),('s','p')]
    choices_dict = {'r':'rock','s':'scissors', 'p':'paper' }
    results_dict = {'win':'win','loss':'lost','draw':'drew'}

    def play(self):
        #get user item
        user_item = self.get_user_item()
        if user_item == 'exit':
            return
        comp_item = self.get_computer_item()
        turn_result = self.get_game_result(user_item,comp_item)
        print(f"""You Selected {self.choices_dict[user_item]}.
The computer selected {self.choices_dict[comp_item]}.
You {self.results_dict[turn_result]}!\n """)
        return turn_result


    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'draw'
        items_tuple = (user_item,computer_item)
        if items_tuple in self.user_victories:
            return 'win'
        return 'loss'


        #longer way
        # if user_item == computer_item:
        #     return 'draw'
        # #if user has paper
        # elif user_item == 'p':
        #     #comp has scissors
        #     if computer_item == 's':
        #         return 'loss'
        #     #comp has rock
        #     else:
        #         return 'win'
        # #if user has rock
        # elif user_item == 'r':
        #     #comp has scissors
        #     if computer_item == 'p':
        #         return 'loss'
        #     #comp has rock
        #     else:
        #         return 'win'
        # #if user has paper
        # elif user_item == 's':
        #     #comp has scissors
        #     if computer_item == 'r':
        #         return 'loss'
        #     #comp has rock
        #     else:
        #         return 'win'
