from game import  Game


def get_user_menu_choice():
    user_menu_choice = input("Hello! choose an option:\np - Play a new game\nc - Show Scores\nq - Quit\n").strip().lower()
    return user_menu_choice

def print_results(results):
    print("Game Results\n")
    print(f"You won {results['win']} times")
    print(f"You lost {results['loss']} times")
    print(f"You drew {results['draw']} times")
    print("\nThank you for playing!\n")



def main():
    game_results = {'win': 0,'loss': 0,'draw': 0}
    while True:
        user_choice = get_user_menu_choice()
        if user_choice == 'p':
            rps = Game()
            result = rps.play()
            if result:
                game_results[result] += 1
            else:
                print("Goodbye, Thanks for playing!")
                break
        if user_choice == 'c' or user_choice == 'q':
            print_results(game_results)
        if user_choice == 'q':
            break

if __name__ == "__main__":
    main()
