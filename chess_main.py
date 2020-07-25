import pygame
import sys
from chess_board import Board
pygame.init()

size = hight, width = 800, 800

surface = pygame.display.set_mode(size)

board = Board()

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                board.get_mouse(pos[0], pos[1], surface)

    
    board.draw(surface)

    pygame.display.flip()