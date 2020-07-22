import pygame
import sys
from chess_board import Board
pygame.init()

size = hight, width = 800, 800

surface = pygame.display.set_mode(size)

board = Board()

board.board[0][3] = "Q"

for y in board.board:
    print(y)

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    
    board.draw(surface)

    pygame.display.flip()