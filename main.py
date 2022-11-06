import copy

def create_board(): 
    board = []
    for i in range(8):
        ligne = []
        for j in range(8):        
            if j % 2 == i % 2:
                ligne.append(f"{chr(j + 97)}{i + 1}")
                #ligne.append("X")
            else:
                ligne.append(f"{chr(j + 97)}{i + 1}")
                #ligne.append("O")
        board.append(ligne)
    return board
    


def display_board(board, pieces):      #  pieces = [[0, 1, "W"], [2, 3, "B"]]
    tmp = copy.deepcopy(board)

    for piece in pieces:
        tmp[piece[0]][piece[1]] = piece[2]

    tmp.reverse()
    for lign in tmp:
        print('  '.join(lign))


bd = create_board()


wx, bx = 0, 7

# whitePawn = [1, 7, "W"]
# blackPawn = [6, 0, "B"]

piece_arr = []

for i in range(8):
    wp = [wx, i, "W"]
    piece_arr.append(wp)

for i in range(8):
    bp = [bx, i, "B"]
    piece_arr.append(bp)




while True:
    display_board(bd, piece_arr)
    move = input("Pick a square")
    proper_column = ord(move[0]) - 97 # gives the column in which to check for pawns


    for piece in piece_arr:
        if piece[1] == proper_column and (piece[0] == int(move[1]) - 1 or piece[0] == int(move[1]) + 1):
            print(f"found the {piece[2]} pawn")
            if piece[2][0] == "W" and piece[0] < int(move[1]):
                piece[0] += 1
            if piece[2][0] == "B" and piece[0] > int(move[1]):
                piece[0] -= 1

                 

# e4  -->  e(4-1) and e(4+1) . 
#          ord(letter) - 97 = 4
#          e = 4
# 4   -->   check row 3 and 5

 