import numpy as np

ROWS = 6
COLS = 7

def create_board():
    board = np.zeros((ROWS, COLS))
    return board

board = create_board()
game_over = False
turn = 0

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[0][col] == 0

def get_next_open_row(board, col):
    for row in range(ROWS-1, -1, -1):
        if board[row][col] == 0:
            return row

def draw_board(board):
    pass

def winning_move(board, piece):
    #horizontal check
    for row in range(ROWS):
        for col in range(COLS-3):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                return True

    #vertical check
    for row in range(ROWS-3):
        for col in range(COLS):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                return True
            

    #top left to bottom right diagonal
    for row in range(ROWS-3):
        for col in range(COLS-3):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                return True

    #bottom left to top right diagonal
    for row in range(3, ROWS):
        for col in range(COLS-3):
            if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                return True

if __name__ == '__main__':            
    while not game_over:
        
        try:
            player = turn+1
            col = int(input(f'player {player}:'))
            if 0<col<=COLS and is_valid_location(board, col-1):
                row = get_next_open_row(board, col-1)
                drop_piece(board, row, col-1, player)

                if winning_move(board, player):
                    print(f'player {player} wins')
                    game_over = True

                turn = (turn + 1)%2

            else:
                print('invalid column try again')
        
        except ValueError:
            print('enter a valid integer')

        print(board)