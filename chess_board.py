import pygame
from chess_pieces import *
from copy import deepcopy

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
        self.update_all_moves(self.board)

    def update_all_moves(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j]:
                    board[i][j].update_moves(board)

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

    def get_oponents_moves(self, board):
        moves = []
        for i in range(8):
            for j in range(8):
                if board[i][j]:
                    if board[i][j].isWhite != self.whites_turn:
                        moves += board[i][j].get_moves()
        return moves

    def locate_king(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] and board[i][j].isKing and board[i][j].isWhite == self.whites_turn:
                    return (j, i)

    def isCheck(self, board):
        position_king = self.locate_king(board)
        all_oponent_moves = self.get_oponents_moves(board)
        if position_king in all_oponent_moves:
            return True

    def reverse_move(self, move, saved_square):
            self.board[self.chosen_piece[1]][self.chosen_piece[0]] = self.board[move[1]][move[1]] 
            self.board[self.chosen_piece[1]][self.chosen_piece[0]].pos = self.chosen_piece
            self.board[move[1]][move[1]] = saved_square 
            self.update_all_moves(self.board)

    def update_legal_moves(self, moves):
        legal_moves = []
        for move in moves:
            if move == self.chosen_piece:
                legal_moves.append(move)
                continue
            saved_square = self.board[move[1]][move[1]]
            self.board[move[1]][move[1]] = self.board[self.chosen_piece[1]][self.chosen_piece[0]]
            self.board[self.chosen_piece[1]][self.chosen_piece[0]] = None
            self.board[move[1]][move[1]].pos = move 
            self.update_all_moves(self.board)
            if self.isCheck(self.board):
                self.reverse_move(move, saved_square)
                continue
            else:
                self.reverse_move(move, saved_square)
                legal_moves.append(move)
        return legal_moves


    def get_mouse(self, x, y, surface):
        x = x // self.square_size
        y = y // self.square_size
        if self.board_moves[y][x]: 
            print(self.board[y][x])
            if self.board[y][x]:
                print(self.board[y][x].pos)
                print(self.chosen_piece)
                if self.board[y][x].pos == self.chosen_piece:
                    return
            self.board[y][x] = self.board[self.chosen_piece[1]][self.chosen_piece[0]]
            self.board[self.chosen_piece[1]][self.chosen_piece[0]] = None
            self.board[y][x].pos = (x, y)
            self.board[y][x].first_move = False
            self.whites_turn = not self.whites_turn
            self.reset_board_moves()
            self.isCheck(self.board)
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