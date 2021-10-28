from math import isnan

def check_valid_num(num, max, min = 0):
    #is num
    if isnan(num):
        return False
    #between range
    if not num in range(min,max):
         return False
    return True

def player_input(current_player_symbol, max_row_num, max_col_num):
    valid_inputs = False

    while not valid_inputs:
        print(f"It's your turn player {current_player_symbol}")
        row_num = int(input(f"Please enter row number (start from 0 to {max_row_num-1}): "))
        col_num = int(input(f"Please enter col number (start from 0 to {max_col_num-1}): "))
        if check_valid_num(row_num, max_row_num) and check_valid_num(col_num, max_col_num):
            break
        else:
            print("Please enter again - your inputs are invalid!")

    return (row_num, col_num)
