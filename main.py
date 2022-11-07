import copy

def create_board(): 
    board = []
    for i in range(8):
        ligne = []
        for j in range(8):        
            if j % 2 == i % 2:
                #ligne.append(f"{chr(j + 97)}{i + 1}")
                ligne.append("X")
            else:
                #ligne.append(f"{chr(j + 97)}{i + 1}")
                ligne.append("O")
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
        wp = [w_x, w_y, "♙", ["v"], 2]
        arr.append(wp)

    for b_x in range(8):
        bp = [b_x, b_y, "♟", ["v"], 2]
        arr.append(bp)

def place_rooks(arr):

    wr = [0, 0, "♖", ["h", "v"], 7]
    wr2 = [7, 0, "♖", ["h", "v"], 7]
    br = [0, 7, "♜", ["h", "v"], 7]
    br2 = [7, 7, "♜", ["h", "v"], 7]
    arr.append(wr)
    arr.append(wr2)
    arr.append(br)
    arr.append(br2)

def place_knights(arr):

    wr = [1, 0, "♘", ["k"], 1]
    wr2 = [6, 0, "♘", ["k"], 1]
    br = [1, 7, "♞", ["k"], 1]
    br2 = [6, 7, "♞", ["k"], 1]
    arr.append(wr)
    arr.append(wr2)
    arr.append(br)
    arr.append(br2)

def place_bishops(arr):

    wr = [2, 0, "♗", ["d"], 7]
    wr2 = [5, 0, "♗", ["d"], 7]
    br = [2, 7, "♝", ["d"], 7]
    br2 = [5, 7, "♝", ["d"], 7]
    arr.append(wr)
    arr.append(wr2)
    arr.append(br)
    arr.append(br2)

def place_queens(arr):
    wq = [3, 0, "♕", ["h", "v", "d"], 7]
    bq = [3, 7, "♛", ["h", "v", "d"], 7]
    arr.append(wq)
    arr.append(bq)

def place_kings(arr):
    wk = [4, 0, "♔", ["h", "v", "d"], 1]
    bk = [4, 7, "♚", ["h", "v", "d"], 1]
    arr.append(wk)
    arr.append(bk)

def is_square_free(x, y, arr):
    for piece in arr:
        if piece[0] == x and piece[1] == y:
            print("Square is not free")
            return 0
    return 1

def how_far_x(start_position, end_position):
    if len(start_position) != 2 or start_position[0].isalpha() == False or start_position[1].isdigit() == False:
        return "invalid start coordinate"
    if len(end_position) != 2 or end_position[0].isalpha() == False or end_position[1].isdigit() == False:
        return "invalid end coordinate"

    nb_of_steps = ord(max(start_position[0], end_position[0])) - ord(min(start_position[0], end_position[0]))

    if end_position[1] == start_position[1]:
        return nb_of_steps
    else:
        return 0

def how_far_y(start_position, end_position):
    if len(start_position) != 2 or start_position[0].isalpha() == False or start_position[1].isdigit() == False:
        return "invalid start coordinate"
    if len(end_position) != 2 or end_position[0].isalpha() == False or end_position[1].isdigit() == False:
        return "invalid end coordinate"

    nb_of_steps = ord(max(start_position[1], end_position[1])) - ord(min(start_position[1], end_position[1]))

    if end_position[0] == start_position[0]:
        return nb_of_steps
    else:
        return 0

def how_far_diagonal(start_position, end_position):
    if len(start_position) != 2 or start_position[0].isalpha() == False or start_position[1].isdigit() == False:
        return "invalid start coordinate"
    if len(end_position) != 2 or end_position[0].isalpha() == False or end_position[1].isdigit() == False:
        return "invalid end coordinate"

    biggest_x_coord = ord(max(start_position[0], end_position[0]))
    smallest_x_coord = ord(min(start_position[0], end_position[0]))
    biggest_y_coord = max(start_position[1], end_position[1])
    smallest_y_coord = min(start_position[1], end_position[1])

    x_substraction = int(biggest_x_coord) - int(smallest_x_coord)
    y_substraction = int(biggest_y_coord) - int(smallest_y_coord)

    if x_substraction == y_substraction:
        return x_substraction
    else:
        return 0

def is_knight_move(start_pos, end_pos):

    max_col = max(ord(start_pos[0]) - 97, ord(end_pos[0]) - 97)
    max_row = max(start_pos[1], end_pos[1])

    min_col = min(ord(start_pos[0]) - 97, ord(end_pos[0]) - 97)
    min_row = min(start_pos[1], end_pos[1])

    if max_col - min_col == 1:
        if int(max_row) - int(min_row) == 2:
            return 1
    if max_col - min_col == 2:
        if int(max_row) - int(min_row) == 1:
            return 1
    return 0

def what_trajectory(start_pos, end_pos):
    if is_knight_move(start_pos, end_pos):
        return("k", 1)
    if how_far_x(start_pos, end_pos):
        return ("h", how_far_x(start_pos, end_pos))
    if how_far_y(start_pos, end_pos):
        return ("v", how_far_y(start_pos, end_pos))
    if how_far_diagonal(start_pos, end_pos):
        return ("d", how_far_diagonal(start_pos, end_pos))
    return "not a move"

bd = create_board()

piece_arr = []
place_pawns(piece_arr)
place_queens(piece_arr)
place_rooks(piece_arr)
place_knights(piece_arr)
place_bishops(piece_arr)
place_kings(piece_arr)

while True:
    display_board(bd, piece_arr)

    move = input("Move it")

    start_x = move[0]
    start_y = move[1]
    end_x = move[2]
    end_y = move[3]

    start_pos = start_x + start_y
    end_pos = end_x + end_y

    print(is_knight_move(start_pos, end_pos))

    for piece in piece_arr:
        if piece[0] == ord(start_x) - ord('a') and piece[1] == int(start_y) - 1: # checks if a piece is on start square
            if is_square_free(ord(end_x) - ord('a'), int(end_y) - 1, piece_arr):  # checks if the end square is free
                if what_trajectory(start_pos, end_pos)[0] in piece[3] and what_trajectory(start_pos, end_pos)[1] <= piece[4]:
                    piece[0] = ord(end_x) - 97
                    piece[1] = int(end_y) - 1
                    if piece[2] == "♙" or piece[2] == "♟":
                        piece[4] = 1
                else:
                    print("that piece does not move like that")


