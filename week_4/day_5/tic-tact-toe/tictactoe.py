
#TIC TAC TOE Game
#Instructions below ↓↓↓

from constants import PLAYER_X_SYMBOL, PLAYER_O_SYMBOL, ROW_NUM, COL_NUM, STARTING_PLAYER_SYMBOL, INVALID_PLACEMENT_MSG
from displayutils import display_welcome_msg, display_game_title, display_board, display_winner_or_draw
from boardutils import generate_board , check_win, get_board_after_placement, is_board_full, is_board_empty_at_row_col
from inpututils import player_input

def play_turn(board,current_symbol, max_row_num, max_col_num):
    display_game_title()
    no_valid_placement_yet = True
    while no_valid_placement_yet:
        row , col = player_input(current_symbol, max_row_num, max_col_num)
        placement_is_valid = is_board_empty_at_row_col(board,row,col)
        if(not placement_is_valid):
            print(INVALID_PLACEMENT_MSG)
        no_valid_placement_yet = not placement_is_valid
    new_board = get_board_after_placement(board,row, col, current_symbol)
    return new_board

def play():
    current_board = generate_board(ROW_NUM,COL_NUM)
    game_won = False
    winner = None
    current_player = STARTING_PLAYER_SYMBOL
    display_welcome_msg()
    while not game_won and not is_board_full(current_board):
        current_board = play_turn(current_board,current_player, ROW_NUM, COL_NUM)
        display_board(current_board)
        if check_win(current_board,current_player):
            game_won = True
            winner = current_player
            break
        if current_player == PLAYER_X_SYMBOL:
            current_player = PLAYER_O_SYMBOL
        else:
            current_player = PLAYER_X_SYMBOL
    display_winner_or_draw(winner)
    return

def main():
    play()

if __name__ == "__main__":
    main()


# What You Will Create
# Create a TicTacToe game in python, where two users can play together.


# Instructions
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

# Hint
# To do this project, you basically need to create four functions:

# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.
# Note: The 4 functions above are just an example. You can implement many more helper
# functions or choose a completely different approach if you want.


# Tips : Consider The Following:
# What functionality will need to occur every turn to make this program work?
# After contemplating the question above, think about splitting your code into smaller pieces (functions).
# Remember to follow the single responsibility principle! each function should do one thing and do it well!
