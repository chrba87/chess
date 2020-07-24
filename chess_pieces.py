import pygame
import os
from collections import namedtuple


class Pieces:
    def __init__(self):
        position = namedtuple('Position', ['x', 'y'])
        self.pos = position(None, None)
        self.square_size = 95
        self.first_move = True

    def add_pos(self, xs, ys):
        pos = tuple(x + y for x, y in zip(xs, ys))
        if 7 < pos[0] or pos[0] < 0:
            return None
        elif 7 < pos[1] or pos[1] < 0:
            return None
        return pos

    def get_moves(self, board):
        return [self.pos]

class Queen_w(Pieces):
    def __init__(self):
        super().__init__()
        self.isWhite = True
        self.pos = (3, 7)
        self.symbol = "Q"
        self.img = pygame.image.load(os.path.join('images', 'w_queen_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))


class Queen_b(Pieces):
    def __init__(self):
        super().__init__()
        self.isWhite = False
        self.symbol = "q"
        self.img = pygame.image.load(os.path.join('images', 'b_queen_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))

class King_w(Pieces):
    def __init__(self):
        super().__init__()
        self.isWhite = True
        self.symbol = "K"
        self.img = pygame.image.load(os.path.join('images', 'w_king_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))


class King_b(Pieces):
    def __init__(self):
        super().__init__()
        self.isWhite = False
        self.symbol = "k"
        self.img = pygame.image.load(os.path.join('images', 'b_king_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))


class Bishop_w(Pieces):
    def __init__(self):
        super().__init__()
        self.isWhite = True
        self.symbol = "B"
        self.img = pygame.image.load(os.path.join('images', 'w_bishop_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))


class Bishop_b(Pieces):
    def __init__(self):
        super().__init__()
        self.isWhite = False
        self.symbol = "b"
        self.img = pygame.image.load(os.path.join('images', 'b_bishop_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))
    

class Knight_w(Pieces):
    def __init__(self):
        super().__init__()
        self.isWhite = True
        self.symbol = "KN"
        self.img = pygame.image.load(os.path.join('images', 'w_knight_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))

class Knight_b(Pieces):
    def __init__(self):
        super().__init__()
        self.isWhite = False
        self.symbol = "kn"
        self.img = pygame.image.load(os.path.join('images', 'b_knight_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))
        
class Rook_w(Pieces):
    def __init__(self):
        super().__init__()
        self.isWhite = True
        self.symbol = "R"
        self.img = pygame.image.load(os.path.join('images', 'w_rook_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))

class Rook_b(Pieces):
    def __init__(self):
        super().__init__()
        self.isWhite = False
        self.symbol = "r"
        self.img = pygame.image.load(os.path.join('images', 'b_rook_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))
        
class Pawn_w(Pieces):
    def __init__(self):
        super().__init__()
        self.isWhite = True
        self.symbol = "P"
        self.img = pygame.image.load(os.path.join('images', 'w_pawn_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))
    
    def get_moves(self, board):
        self.move = (0, -1)
        self.cap1 = (-1, -1)
        self.cap2 = (1, -1)
        moves = [self.pos]
        new_pos = self.add_pos(self.pos, self.move)
        new_cap1 = self.add_pos(self.pos, self.cap1)
        if new_cap1:
            if board[new_cap1[1]][new_cap1[0]]:
                if board[new_cap1[1]][new_cap1[0]].isWhite == False:
                    moves.append(new_cap1)
        new_cap2 = self.add_pos(self.pos, self.cap2)
        if new_cap2:
            if board[new_cap2[1]][new_cap2[0]]:
                if board[new_cap2[1]][new_cap2[0]].isWhite == False:
                    moves.append(new_cap2)
        if board[new_pos[1]][new_pos[0]]:
            return moves
        else:
            moves.append(new_pos)
        if self.first_move:
            new_pos = self.add_pos(new_pos, self.move)
            if board[new_pos[1]][new_pos[0]]:
                return moves
            else:
                moves.append(new_pos)
        return moves

        
class Pawn_b(Pieces):
    def __init__(self):
        super().__init__()
        self.isWhite = False
        self.symbol = "p"
        self.img = pygame.image.load(os.path.join('images', 'b_pawn_png_512px.png'))
        self.img = pygame.transform.scale(self.img, (self.square_size, self.square_size))

    def get_moves(self, board):
        self.move = (0, 1)
        self.cap1 = (-1, 1)
        self.cap2 = (1, 1)
        moves = [self.pos]
        new_pos = self.add_pos(self.pos, self.move)
        new_cap1 = self.add_pos(self.pos, self.cap1)
        if new_cap1:
            if board[new_cap1[1]][new_cap1[0]]:
                if board[new_cap1[1]][new_cap1[0]].isWhite == True:
                    moves.append(new_cap1)
        new_cap2 = self.add_pos(self.pos, self.cap2)
        if new_cap2:
            if board[new_cap2[1]][new_cap2[0]]:
                if board[new_cap2[1]][new_cap2[0]].isWhite == True:
                    moves.append(new_cap2)
        if board[new_pos[1]][new_pos[0]]:
            return moves
        else:
            moves.append(new_pos)
        if self.first_move:
            new_pos = self.add_pos(new_pos, self.move)
            if board[new_pos[1]][new_pos[0]]:
                return moves
            else:
                moves.append(new_pos)
        return moves