import pygame
import os
from collections import namedtuple


class Pieces:
    def __init__(self, x, y, isWhite):
        self.pos = (x, y) 
        self.isWhite = isWhite
        self.square_size = 96
        self.first_move = True
        self.isKing = False
        self.possible_moves = [self.pos]

    def add_pos(self, xs, ys):
        pos = tuple(x + y for x, y in zip(xs, ys))
        if 7 < pos[0] or pos[0] < 0:
            return None
        elif 7 < pos[1] or pos[1] < 0:
            return None
        return pos

    def update_single_step_moves(self, board):
        self.possible_moves = [self.pos]
        for d in self.directions:
            new_pos = self.add_pos(self.pos, d)
            if new_pos:
                if board[new_pos[1]][new_pos[0]]:
                    if board[new_pos[1]][new_pos[0]].isWhite != self.isWhite:
                        self.possible_moves.append(new_pos)
                else:
                    self.possible_moves.append(new_pos)

    def update_recursive_moves(self, board):
        self.possible_moves = [self.pos]
        for direction in self.directions:
            self.possible_moves += self.check_recursive(self.pos, direction, board)


    def check_recursive(self, pos, dir, board):
        new_pos = self.add_pos(pos, dir)
        if not new_pos:
            return []
        if board[new_pos[1]][new_pos[0]]:
            if board[new_pos[1]][new_pos[0]].isWhite == self.isWhite:
                return []
            else:
                return [new_pos]
        else:
            moves = [new_pos] + self.check_recursive(new_pos, dir, board)
        return moves

    def __repr__(self):
        return self.symbol


class Queen(Pieces):
    def __init__(self, x, y, isWhite):
        super().__init__(x, y, isWhite)
        self.symbol = "Q"
        if isWhite:
            self.img = pygame.image.load(os.path.join('images', 'w_queen_png_512px.png'))
        else:
            self.img = pygame.image.load(os.path.join('images', 'b_queen_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))
        self.directions = [(1, 0), (-1, 0), (0, 1), (0 , -1), (1, 1), (-1, -1), (1, -1), (-1 , 1)]

    def update_moves(self, board):
        self.update_recursive_moves(board)


class King(Pieces):
    def __init__(self, x, y, isWhite):
        super().__init__(x, y, isWhite)
        self.isKing = True
        self.symbol = "K"
        if isWhite:
            self.img = pygame.image.load(os.path.join('images', 'w_king_png_512px.png'))
        else:
            self.img = pygame.image.load(os.path.join('images', 'b_king_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))
        self.directions = [(1, 0), (-1, 0), (0, 1), (0 , -1), (1, 1), (-1, -1), (1, -1), (-1 , 1)]

    def update_moves(self, board):
        self.update_single_step_moves(board)


class Bishop(Pieces):
    def __init__(self, x, y, isWhite):
        super().__init__(x, y, isWhite)
        self.symbol = "B"
        if isWhite:
            self.img = pygame.image.load(os.path.join('images', 'w_bishop_png_512px.png'))
        else:
            self.img = pygame.image.load(os.path.join('images', 'b_bishop_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))
        self.directions = [(1, 1), (-1, -1), (1, -1), (-1 , 1)]

    def update_moves(self, board):
        self.update_recursive_moves(board)


class Knight(Pieces):
    def __init__(self, x, y, isWhite):
        super().__init__(x, y, isWhite)
        self.symbol = "KN"
        if isWhite:
            self.img = pygame.image.load(os.path.join('images', 'w_knight_png_512px.png'))
        else:
            self.img = pygame.image.load(os.path.join('images', 'b_knight_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))
        self.directions = [(2, 1), (2, -1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (-1, -2)]

    def update_moves(self, board):
        self.update_single_step_moves(board)


class Rook(Pieces):
    def __init__(self, x, y, isWhite):
        super().__init__(x, y, isWhite)
        self.symbol = "R"
        if isWhite:
            self.img = pygame.image.load(os.path.join('images', 'w_rook_png_512px.png'))
        else:
            self.img = pygame.image.load(os.path.join('images', 'b_rook_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))
        self.directions = [(1, 0), (-1, 0), (0, 1), (0 , -1)]

    def update_moves(self, board):
        self.update_recursive_moves(board)


class Pawn(Pieces):
    def __init__(self, x, y, isWhite):
        super().__init__(x, y, isWhite)
        self.symbol = "P"
        if isWhite:
            self.img = pygame.image.load(os.path.join('images', 'w_pawn_png_512px.png'))
            self.move = (0, -1)
            self.caps = [(-1, -1), (1, -1)]
        else:
            self.img = pygame.image.load(os.path.join('images', 'b_pawn_png_512px.png'))
            self.move = (0, 1)
            self.caps = [(1, 1), (1, -1)]
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))
    
    def update_moves(self, board):
        self.possible_moves = [self.pos]
        for cap in self.caps:
            new_cap = self.add_pos(self.pos, cap)
            if new_cap:
                if board[new_cap[1]][new_cap[0]]:
                    if board[new_cap[1]][new_cap[0]].isWhite != self.isWhite:
                        self.possible_moves.append(new_cap)
        new_pos = self.add_pos(self.pos, self.move)
        if board[new_pos[1]][new_pos[0]]:
            return 
        else:
            self.possible_moves.append(new_pos)
        if self.first_move:
            new_pos = self.add_pos(new_pos, self.move)
            if board[new_pos[1]][new_pos[0]]:
                return 
            else:
                self.possible_moves.append(new_pos)
        