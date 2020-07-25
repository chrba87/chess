import pygame
from chess_pieces import *
from copy import deepcopy
from itertools import product

class Board:
    def __init__(self):
        self.board = [[None for x in range(8)] for y in range(8)]
        self.square_size = 100
        self.whites_turn = True
        self.img_board_light = pygame.image.load(os.path.join('images', 'square_gray_light_png_512px.png'))
        self.img_board_light = pygame.transform.scale(self.img_board_light, (self.square_size, self.square_size))
        self.img_board_dark = pygame.image.load(os.path.join('images', 'square_gray_dark_png_512px.png'))
        self.img_board_dark = pygame.transform.scale(self.img_board_dark, (self.square_size, self.square_size))
        self.initiate_board()
        self.reset_board_moves()

    def reset_board_moves(self):
        self.chosen_piece = (None, None)
        self.board_moves = [[None for x in range(8)] for y in range(8)]
        self.update_all_moves()

    def update_all_moves(self):
        for i, j in product(range(8), range(8)):
            if self.board[i][j]:
                self.board[i][j].update_moves(self.board)

    def initiate_board(self):
        self.board[7][3] = Queen_w(3, 7)
        self.board[0][3] = Queen_b(3, 0)
        self.board[7][4] = King_w(4, 7)
        self.board[0][4] = King_b(4, 0)
        self.board[7][2] = Bishop_w(2, 7)
        self.board[0][2] = Bishop_b(2, 0)
        self.board[7][5] = Bishop_w(5, 7)
        self.board[0][5] = Bishop_b(5, 0)
        self.board[7][1] = Knight_w(1, 7)
        self.board[0][1] = Knight_b(1, 0)
        self.board[7][6] = Knight_w(6, 7)
        self.board[0][6] = Knight_b(6, 0)
        self.board[7][0] = Rook_w(0, 7)
        self.board[0][0] = Rook_b(0, 0)
        self.board[7][7] = Rook_w(7, 7)
        self.board[0][7] = Rook_b(7, 0)
        for i in range(8):
            self.board[1][i] = Pawn_b(i, 1)
            self.board[6][i] = Pawn_w(i, 6)

    def draw(self, surface):
        dark = True
        for i in range(8): 
            dark = not dark
            for j in range(8):
                if dark:
                    surface.blit(self.img_board_dark, (j*self.square_size, i*self.square_size))
                else:
                    surface.blit(self.img_board_light, (j*self.square_size, i*self.square_size))
                dark = not dark
                if self.board_moves[i][j]:
                    pygame.draw.rect(surface, (0, 255, 50), (j * self.square_size, i * self.square_size, self.square_size, self.square_size), 5)
                if self.board[i][j]:
                    surface.blit(self.board[i][j].img, (j*self.square_size+2, i*self.square_size+2))

    def get_oponents_moves(self):
        return [m for x in [self.board[i][j].get_moves() for i, j in product(range(8), range(8)) if self.board[i][j] and self.board[i][j].isWhite != self.whites_turn] for m in x]

    def locate_king(self):
        for i, j in product(range(8), range(8)):
            if self.board[i][j] and self.board[i][j].isKing and self.board[i][j].isWhite == self.whites_turn:
                return (j, i)

    def isMate(self):
        saved_chosen = self.chosen_piece
        moves = []
        for i, j in product(range(8), range(8)):
            if self.board[i][j] and self.board[i][j].isWhite == self.whites_turn:
                self.chosen_piece = (j, i)
                moves += self.update_legal_moves([x for x in self.board[i][j].get_moves() if x != self.chosen_piece])
        self.chosen_piece = saved_chosen
        if len(moves) == 0:
            print("Checkmate!")
            return True
        else:
            return False

    def isCheck(self):
        position_king = self.locate_king()
        all_oponent_moves = self.get_oponents_moves()
        if position_king in all_oponent_moves:
            return True

    def reverse_move(self, move, saved_square):
        self.move(move, self.chosen_piece)
        self.board[move[1]][move[0]] = saved_square 
        self.update_all_moves()

    def update_legal_moves(self, moves):
        legal_moves = []
        for move in moves:
            if move == self.chosen_piece:
                legal_moves.append(move)
                continue
            saved_square = self.board[move[1]][move[0]]
            self.move(self.chosen_piece, move)
            self.update_all_moves()
            if self.isCheck():
                self.reverse_move(move, saved_square)
                continue
            else:
                self.reverse_move(move, saved_square)
                legal_moves.append(move)
        return legal_moves

    def move(self, from_x_y, to_x_y):
        self.board[to_x_y[1]][to_x_y[0]] = self.board[from_x_y[1]][from_x_y[0]]
        self.board[from_x_y[1]][from_x_y[0]] = None
        self.board[to_x_y[1]][to_x_y[0]].pos = to_x_y


    def get_mouse(self, x, y, surface):
        x = x // self.square_size
        y = y // self.square_size
        if self.board_moves[y][x]: 
            if self.board[y][x] and self.board[y][x].pos == self.chosen_piece:
                return
            self.move(self.chosen_piece, (x, y))
            self.board[y][x].first_move = False
            self.isCheck()
            self.whites_turn = not self.whites_turn
            self.isMate()
            self.reset_board_moves()
            return
        else:
            self.reset_board_moves()
        if self.board[y][x]:
            if self.board[y][x].isWhite != self.whites_turn:
                return
            self.chosen_piece = (x, y)
            moves = self.board[y][x].get_moves()
            moves = self.update_legal_moves(moves)
            for move in moves:
                self.board_moves[move[1]][move[0]] = True