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

def place_pawns(arr):
    
    w_y, b_y = 1, 6

    for w_x in range(8):
        wp = [w_x, w_y, "WP"]
        arr.append(wp)

    for b_x in range(8):
        bp = [b_x, b_y, "BP"]
        arr.append(bp)

def place_queens(arr):
    w_y = 0
    for w_x in range(8):
        wq = [w_x, w_y, "WQ"]
        arr.append(wq)

def is_square_free(x, y, arr):
    for piece in arr:
        if piece[0] == x and piece[1] == y:
            print("not free")
            return 0
    print("free")
    return 1

bd = create_board()

piece_arr = []
place_pawns(piece_arr)
place_queens(piece_arr)


while True:
    display_board(bd, piece_arr)
    move = input("Move it")

    start_x = move[0]
    start_y = move[1]
    end_x = move[2]
    end_y = move[3]

    for piece in piece_arr:
        if piece[0] == ord(start_x) - 97 and piece[1] == int(start_y) - 1 and is_square_free(ord(end_x) - 97, int(end_y) - 1, piece_arr):
            piece[0] = ord(end_x) - 97
            piece[1] = int(end_y) - 1


