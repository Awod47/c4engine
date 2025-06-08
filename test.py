import numpy as np

def create_board():
    board = np.zeros((6,7))
    return board

def is_valid_col(board, col):
    return board[0][col] == 0

def drop_piece(board, col, row, player):
    board[row][col] = player

def get_valid_row(board, col):
    for r in range(5, -1, -1):
        if board[r][col] == 0:
            return r

board = create_board()
game_over = False
turn = 0

while not game_over:
    player = turn+1
    col = int(input(f'player {player} move: '))
    if 0<=col<7 and is_valid_col(board, col):
        row = get_valid_row(board, col)
        drop_piece(board, col, row, player)


    print(board)