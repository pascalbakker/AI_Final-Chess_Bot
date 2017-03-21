import chess

def startGame():
    #clear_stack()
    return chess.Board()

def displayBoard(board):
    print board

def main():
    init_board = startGame()
    displayBoard(init_board)

    stillPlaying = True     # outer loop boolean
    player_white = True     # white player turn
    player_black = False    # black player turn

    while stillPlaying:

        if player_white:
            print "white moves"

        else:
            print "black moves"

main()
