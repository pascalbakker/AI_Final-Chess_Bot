
import chess
import random

def randomAI(board): #Selects one of the legal moves randomly and returns it
    moves = []
    #Creates list of legal moves
    for move in board.legal_moves:
        moves.append(move)
    move = random.choice(moves)
    while not chess.Move.from_uci(str(move)) in board.legal_moves:
        move = random.choice(moves)

    return chess.Move.from_uci(str(move))



#Runs the chess game until win, draw, or stalemate
if __name__ == "__main__":
    board = chess.Board()
    color = True #True=White False=Black
    num = 0 #Number of moves
    while(True):
        board.push(randomAI(board))
        num=num+1
        print board
        if board.is_stalemate() or board.is_insufficient_material() or board.can_claim_threefold_repetition() or board.can_claim_fifty_moves() or board.can_claim_draw():
            print "Stalemate or Draw"
            print "Number of Moves: ",num
            break;
            if board.is_game_over() or board.is_checkmate():
                if color:
                    print "White Won"
                else:
                    print "Black Won"
                print "Number of Moves: ",num
                break;
        color=not color
