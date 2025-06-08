import pygame
import sys
import numpy as np
from connect4 import create_board, is_valid_location, get_next_open_row, drop_piece, winning_move 
from random_move import random_ai

colors = {
    'BOARD': (104,16,73),
    'PLAYER1': (255, 0, 0),
    'PLAYER2': (255, 255, 0),
    'BLACK': (0,0,0)
}


COLS = 7
ROWS = 6

pygame.init()
my_font = pygame.font.SysFont('monospace', 75)

SQUARE_SIZE = 100

width = COLS * SQUARE_SIZE
height = (ROWS+1) * SQUARE_SIZE
size = (width, height)

board = create_board()
game_over = False
turn = 0

def draw_board(board):
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, colors.get('BOARD'), (col * SQUARE_SIZE, row * SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[row][col] == 0:
                pygame.draw.circle(screen, colors.get('BLACK'), (col * SQUARE_SIZE+SQUARE_SIZE/2, (row+1) * SQUARE_SIZE+SQUARE_SIZE/2), (SQUARE_SIZE/2)-5)
            elif board[row][col] == 1:
                pygame.draw.circle(screen, colors.get('PLAYER1'), (col * SQUARE_SIZE+SQUARE_SIZE/2, (row+1) * SQUARE_SIZE+SQUARE_SIZE/2), (SQUARE_SIZE/2)-5)
            if board[row][col] == 2:
                pygame.draw.circle(screen, colors.get('PLAYER2'), (col * SQUARE_SIZE+SQUARE_SIZE/2, (row+1) * SQUARE_SIZE+SQUARE_SIZE/2), (SQUARE_SIZE/2)-5)

    pygame.display.update()


screen = pygame.display.set_mode(size)
draw_board(board)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            try:
                player = turn+1
                col = int(event.pos[0]//100) #this gets the mouse position through event.pos and converts it to a number from 0-6 for columns
                print(player)
                if 0<=col<COLS and is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, player)
                    draw_board(board)

                    if winning_move(board, player):
                        print(f'player {player} wins')
                        label = my_font.render(f'Player {player} wins', 1, colors.get(f'PLAYER{player}'))
                        screen.blit(label, (40,10))
                        pygame.display.update()
                        pygame.time.wait(3000)
                        game_over = True

                    print(board)
                    turn = (turn + 1)%2

                else:
                    print('invalid column try again')
            
            except ValueError:
                print('enter a valid integer')

    if turn == 1 and not game_over:
        player = 2
        col = random_ai(board)
        if col is not None:
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, player)
            draw_board(board)

            if winning_move(board, player):
                print('ai wins')
                label = my_font.render(f'AI wins', 1, colors.get(f'PLAYER2'))
                screen.blit(label, (40,10))
                pygame.display.update()
                pygame.time.wait(3000)
                game_over = True

            print(board)
            turn = (turn + 1)%2

        else:
            print('no more columns left')
            game_over = True