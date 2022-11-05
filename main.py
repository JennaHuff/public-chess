import board
import copy

# --+---+---+---+---+---+---+--
# X | O | X | O | X | O | X | O
# --+---+---+---+---+---+---+--
# B | B | B | B | B | B | B | B
# --+---+---+---+---+---+---+--
# X O X O X O X O
# O X O X O X O X
# X O X O X O X O
# O X O X O X O W
# W W W W W W W W
# O X O X O X O X

def create_board(): 
    board = []
    for i in range(8):
        ligne = []
        for j in range(8):        
            if j % 2 == i % 2:
                ligne.append("X")
            else:
                ligne.append("O")
        board.append(ligne)
    return board
    


def display_board(board, pieces):      #  pieces = [[0, 1, "W"], [2, 3, "B"]]
    tmp = copy.deepcopy(board)


    for piece in pieces:
        tmp[piece[0]][piece[1]] = piece[2]

    for lign in tmp:
        print('  '.join(lign))




bd = create_board()

wx, bx = 0, 7

# whitePawn = [1, 7, "W"]
# blackPawn = [6, 0, "B"]

piece_arr = []

for i in range(8):
    wp = [0, i, "W"]
    piece_arr.append(wp)

for i in range(8):
    bp = [7, i, "B"]
    piece_arr.append(bp)



while True:
    display_board(bd, piece_arr)
    move = input("black or white ?")
    if move[0] == "w":
        piece_arr[7-int(move[1])][0] += 1 
    elif move[0] == "b":
        piece_arr[8 + int(move[1])][0] -= 1 


        
 