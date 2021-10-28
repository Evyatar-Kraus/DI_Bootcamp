from constants import BOARD_EMPTY_SPACE_SYMBOL

#generate empty board with a specific number of rows and specific number of columns inside
def generate_board(row_num,col_num):
    board = [[' ' for x in range(0, col_num)] for y in range(0, row_num)]
    return board

#receives a board and a location - row and column - and a symbol; returns it after placing the symbol
def get_board_after_placement(board,row,col,symbol):
    new_board = [row[:] for row in board]
    new_board[row][col] = symbol
    return new_board

#checks the board for an horizontal win
def check_horizontal_row_win(board, symbol):
    for row in board:
        if row.count(symbol) == len(row):
            return True
    return False

#checks the board for an vettical win
def check_vertical_row_win(board, symbol):
    rotated_board = list(zip(*board))
    return check_horizontal_row_win(rotated_board, symbol)

#check the board for a diagonal win of type #1
def check_diagonal_win_left_up_to_right_bottom(board, symbol):
    for rowIdx, row in enumerate(board):
        for colIdx, currentSymbol in enumerate(row):
            if rowIdx == colIdx and currentSymbol != symbol:
                    return False
    return True

#check the board for a diagonal win of type #2
def check_diagonal_win_left_bottom_to_right_up(board, symbol):
    for rowIdx, row in enumerate(board):
        for colIdx, currentSymbol in enumerate(row):
            if colIdx == (len(board[0]) - 1 - rowIdx) and currentSymbol != symbol:
                return False
    return True

#check the board for any diagonal win
def check_diagonal_win(board, symbol):
    return check_diagonal_win_left_up_to_right_bottom(board, symbol) or\
         check_diagonal_win_left_bottom_to_right_up(board, symbol)

#checks if the board is empty and able to place a symbol at a given location
is_board_empty_at_row_col = lambda board,row,col: board[row][col] == BOARD_EMPTY_SPACE_SYMBOL

def is_board_full(board):
    for row in board:
        for col in row:
            if col == BOARD_EMPTY_SPACE_SYMBOL:
                return False
    return True

def check_win(board, current_player_symbol):
    game_won = False
    game_won = check_horizontal_row_win(board, current_player_symbol) or \
        check_vertical_row_win(board, current_player_symbol) or \
        check_diagonal_win(board, current_player_symbol)
    return game_won
