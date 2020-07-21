import chess
import chess.svg
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

board = chess.Board()

while True:
    cls()
    print(board)
    move = input('Enter your move: ')
    if move == 'sniper':
        target = int(input('Enter target square: '))
        board.remove_piece_at(target)
    elif move == 'add':
        target = int(input('Enter target square: '))
        piece = input('Enter piece to add: ')
        board.set_piece_at(target, chess.Piece.from_symbol(piece))
    else:
        try:
            board.push_san(move)
        except: pass