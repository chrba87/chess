import pygame

class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for x in range(8)]
        self.square_size = 100


    def draw(self, surface):
        fill = True
        for i in range(8): 
            fill = not fill
            for j in range(8):
                if fill:
                    pygame.draw.rect(surface, (0, 0, 0), (j * self.square_size, i * self.square_size, self.square_size, self.square_size))
                else:
                    pygame.draw.rect(surface, (255, 255, 255), (j * self.square_size, i * self.square_size, self.square_size, self.square_size))
                fill = not fill