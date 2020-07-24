import pygame
from chess_pieces import *

class Board:
    def __init__(self):
        self.board = [[None for x in range(8)] for y in range(8)]
        self.square_size = 100
        self.whites_turn = True
        self.initiate_board()
        self.reset_board_moves()

    def reset_board_moves(self):
        self.chosen_piece = (None, None)
        self.board_moves = [[None for x in range(8)] for y in range(8)]

    def initiate_board(self):
        self.board[7][3] = Queen_w()
        self.board[7][3].pos = (3, 7)
        self.board[0][3] = Queen_b()
        self.board[0][3].pos = (3, 0)
        self.board[7][4] = King_w()
        self.board[7][4].pos = (4, 7)
        self.board[0][4] = King_b()
        self.board[0][4].pos = (4, 0)
        self.board[7][2] = Bishop_w()
        self.board[7][2].pos = (2, 7)
        self.board[0][2] = Bishop_b()
        self.board[0][2].pos = (2, 0)
        self.board[7][5] = Bishop_w()
        self.board[7][5].pos = (5, 7)
        self.board[0][5] = Bishop_b()
        self.board[0][5].pos = (5, 0)
        self.board[7][1] = Knight_w()
        self.board[7][1].pos = (1, 7)
        self.board[0][1] = Knight_b()
        self.board[0][1].pos = (1, 0)
        self.board[7][6] = Knight_w()
        self.board[7][6].pos = (6, 7)
        self.board[0][6] = Knight_b()
        self.board[0][6].pos = (6, 0)
        self.board[7][0] = Rook_w()
        self.board[7][0].pos = (0, 7)
        self.board[0][0] = Rook_b()
        self.board[0][0].pos = (0, 0)
        self.board[7][7] = Rook_w()
        self.board[7][7].pos = (7, 7)
        self.board[0][7] = Rook_b()
        self.board[0][7].pos = (7, 0)
        for i in range(8):
            self.board[1][i] = Pawn_b()
            self.board[1][i].pos = (i, 1)
            self.board[6][i] = Pawn_w()
            self.board[6][i].pos = (i, 6)


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
                if self.board_moves[i][j]:
                    pygame.draw.rect(surface, (0, 255, 0), (j * self.square_size, i * self.square_size, self.square_size, self.square_size), 5)
                if self.board[i][j]:
                    surface.blit(self.board[i][j].img, (j*self.square_size, i*self.square_size))


    def get_mouse(self, x, y, surface):
        x = x // self.square_size
        y = y // self.square_size
        
        if self.board_moves[y][x]: 
            if self.board[y][x]:
                if self.board[y][x].pos == self.chosen_piece:
                    return
            self.board[y][x] = self.board[self.chosen_piece[1]][self.chosen_piece[0]]
            self.board[self.chosen_piece[1]][self.chosen_piece[0]] = None
            self.reset_board_moves()
            self.board[y][x].pos = (x, y)
            self.board[y][x].first_move = False
            self.whites_turn = not self.whites_turn
            return
        else:
            self.reset_board_moves()
        if self.board[y][x]:
            if self.board[y][x].isWhite != self.whites_turn:
                return
            self.chosen_piece = (x, y)
            moves = self.board[y][x].get_moves(self.board)
            for move in moves:
                self.board_moves[move[1]][move[0]] = True