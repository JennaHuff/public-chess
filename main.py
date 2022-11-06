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
        tmp[piece[1]][piece[0]] = piece[2]

    tmp.reverse()
    for lign in tmp:
        print('  '.join(lign))


bd = create_board()

w_y, b_y = 0, 7

piece_arr = []

for w_x in range(8):
    wp = [w_x, w_y, "WP"]
    piece_arr.append(wp)

for b_x in range(8):
    bp = [b_x, b_y, "BP"]
    piece_arr.append(bp)




while True:
    display_board(bd, piece_arr)
    move = input("Pick a square")
    proper_column = ord(move[0]) - 97 # gives the column in which to check for pawns
    human_move = int(move[1]) - 1
    colision_counter = 0


    for piece in piece_arr:
        if piece[0] == proper_column and (piece[1] == human_move - 1 or piece[1] == human_move + 1):
            print(f"found the {piece[2]} pawn")
            if piece[2][0] == "W" and piece[1] < human_move:
                piece[1] += 1
                colision_counter += 1
            if piece[2][0] == "B" and piece[1] > human_move:
                piece[1] -= 1
                colision_counter += 1
        if colision_counter > 1:
            piece[2] = "#"
            colision_counter = 0


