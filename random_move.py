import random
from connect4 import is_valid_location, get_next_open_row

def random_ai(board):

    valid_columns = [col for col in range(7) if is_valid_location(board, col)]
    if not valid_columns:
        return
    
    col = random.choice(valid_columns)
    return col



