from pprint import pprint
from constants import DEFAULT_WELCOME_MSG, DEFAULT_GAME_TITLE, DEFAULT_DRAW_MSG

def display_welcome_msg(welcomeMsg = None):
    welcomeMsg = welcomeMsg if welcomeMsg else DEFAULT_WELCOME_MSG
    print(welcomeMsg)

def display_game_title(gameTitle = None):
    gameTitle = gameTitle if gameTitle else DEFAULT_GAME_TITLE
    print(gameTitle)

def display_board(board):
    for row in board:
        pprint(row)

def display_winner_or_draw(winner_symbol):
    endMsg = f"The winner is {winner_symbol}!" if winner_symbol else DEFAULT_DRAW_MSG
    print(endMsg)
