import pygame
import os


class Game:
    def __init__(self, board):
        self.board = board
        self.img_board_light = pygame.image.load(os.path.join('images', 'square_gray_light_png_512px.png'))
        self.img_board_light = pygame.transform.scale(self.img_board_light, (self.board.square_size, self.board.square_size))
        self.img_board_dark = pygame.image.load(os.path.join('images', 'square_gray_dark_png_512px.png'))
        self.img_board_dark = pygame.transform.scale(self.img_board_dark, (self.board.square_size, self.board.square_size))


    def draw(self, surface):
        dark = True
        for i in range(8): 
            dark = not dark
            for j in range(8):
                if dark:
                    surface.blit(self.img_board_dark, (j*self.board.square_size, i*self.board.square_size))
                else:
                    surface.blit(self.img_board_light, (j*self.board.square_size, i*self.board.square_size))
                dark = not dark
                if self.board.board_moves[i][j]:
                    pygame.draw.rect(surface, (0, 255, 50), (j * self.board.square_size, i * self.board.square_size, self.board.square_size, self.board.square_size), 5)
                if self.board.board[i][j]:
                    surface.blit(self.board.board[i][j].img, (j*self.board.square_size+2, i*self.board.square_size+2))
