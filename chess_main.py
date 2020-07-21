import pygame
import sys

pygame.init()

size = hight, width = 800, 800

surface = pygame.display.set_mode(size)

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    
    surface.fill((0, 0, 0))

    pygame.display.flip()