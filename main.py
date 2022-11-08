import copy
import os


dead_white_pieces = []
dead_black_pieces = []

def create_board(): 
    board = []
    for i in range(8):
        ligne = []
        for j in range(8):
            if j % 2 == i % 2:
                #ligne.append(f"{chr(j + 97)}{i + 1}")
                ligne.append("+")
            else:
                #ligne.append(f"{chr(j + 97)}{i + 1}")
                ligne.append(" ")
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
        wp = [w_x, w_y, "♙", ["v"], 2, 1] # 2 = range, 1 = white
        arr.append(wp)

    for b_x in range(8):
        bp = [b_x, b_y, "♟", ["v"], 2, 2]
        arr.append(bp)

def place_rooks(arr):

    wr = [0, 0, "♖", ["h", "v"], 7, 1]
    wr2 = [7, 0, "♖", ["h", "v"], 7, 1]
    br = [0, 7, "♜", ["h", "v"], 7, 2]
    br2 = [7, 7, "♜", ["h", "v"], 7, 2]
    arr.append(wr)
    arr.append(wr2)
    arr.append(br)
    arr.append(br2)

def place_knights(arr):

    wr = [1, 0, "♘", ["k"], 1, 1]
    wr2 = [6, 0, "♘", ["k"], 1, 1]
    br = [1, 7, "♞", ["k"], 1, 2]
    br2 = [6, 7, "♞", ["k"], 1, 2]
    arr.append(wr)
    arr.append(wr2)
    arr.append(br)
    arr.append(br2)

def place_bishops(arr):

    wr = [2, 0, "♗", ["d"], 7, 1]
    wr2 = [5, 0, "♗", ["d"], 7, 1]
    br = [2, 7, "♝", ["d"], 7, 2]
    br2 = [5, 7, "♝", ["d"], 7, 2]
    arr.append(wr)
    arr.append(wr2)
    arr.append(br)
    arr.append(br2)

def place_queens(arr):
    wq = [3, 0, "♕", ["h", "v", "d"], 7, 1]
    bq = [3, 7, "♛", ["h", "v", "d"], 7, 2]
    arr.append(wq)
    arr.append(bq)

def place_kings(arr):
    wk = [4, 0, "♔", ["h", "v", "d"], 1, 1]
    bk = [4, 7, "♚", ["h", "v", "d"], 1, 2]
    arr.append(wk)
    arr.append(bk)

def is_square_free(x, y, arr, moving_piece):
    for piece in arr:
        if piece[0] == x and piece[1] == y:
            if piece[5] != moving_piece[5]:
                print(f"{moving_piece[2]} takes {piece[2]}")
                if piece[5] == 1:
                    dead_white_pieces.append(piece[2])
                else:
                    dead_black_pieces.append(piece[2])
                arr.remove(piece)
                return 1
            return 0
    return 1

def how_far_x(start_pos, end_pos):
    if start_pos[1] == end_pos[1]:
        nb_of_steps = abs(start_pos[0] - end_pos[0])
        return nb_of_steps
    else:
        return 0

def how_far_y(start_pos, end_pos):
    if end_pos[0] == start_pos[0]:
        nb_of_steps = abs(start_pos[1] - end_pos[1])
        return nb_of_steps
    else:
        return 0

def how_far_diagonal(start_pos, end_pos):
    x_compare = abs(start_pos[0] - end_pos[0])
    y_compare = abs(start_pos[1] - end_pos[1])
    if x_compare == y_compare:
        nb_of_steps = x_compare
        return nb_of_steps
    else:
        return 0

def is_knight_move(start_pos, end_pos):
    if abs(start_pos[0] - end_pos[0]) == 1:
        if abs(start_pos[1] - end_pos[1]) == 2:
            return 1
    if abs(start_pos[0] - end_pos[0]) == 2:
        if abs(start_pos[1] - end_pos[1]) == 1:
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

def is_way_free(start_pos, end_pos, arr):
    traj = what_trajectory(start_pos, end_pos)  # ex: ("v", 5)
    biggest_y = int(max(start_pos[1], end_pos[1]))
    smallest_y = int(min(start_pos[1], end_pos[1]))
    biggest_x = max(start_pos[0], end_pos[0])
    smallest_x = min(start_pos[0], end_pos[0])

    if traj[0] == "v":
        for piece in arr:
            if piece[0] == end_pos[0] and piece[1] > smallest_y and piece[1] < biggest_y:
                print("vertical not free")
                return 0
        return 1
    if traj[0] == "h":
        for piece in arr:
            if piece[1] == biggest_y and piece[0] > smallest_x and piece[0] < biggest_x:
                print("horizontal not free")
                print(f"piece captures {piece[2]}")
                return 0
        return 1
    if traj[0] == "d":
        for piece in arr:
            piece_coords = []
            piece_coords.append(piece[0])
            piece_coords.append(piece[1])
            if how_far_diagonal(piece_coords, start_pos) and how_far_diagonal(piece_coords, end_pos) and piece[0] > smallest_x and piece[0] < biggest_x:
                print("diagonal not free")
                print(f"piece captures {piece[2]}")
                return 0
        return 1


bd = create_board()

piece_arr = []
place_pawns(piece_arr)
place_queens(piece_arr)
place_rooks(piece_arr)
place_knights(piece_arr)
place_bishops(piece_arr)
place_kings(piece_arr)

def get_command():
    while True:
        move = input("Move it")
        if len(move) != 4:
            continue
        x1 = move[0]
        y1 = move[1]
        x2 = move[2]
        y2 = move[3]
        try:
            y1 = int(y1)
            y2 = int(y2)
        except:
            print('Input should look like this: "a1h8"')
            continue
        if y1 < 1 or y1 > 8 or y2 < 1 or y2 > 8:
            print("Rows are within 1 and 8")
            continue
        if x1 < 'a' or x1 > 'h' or x2 < 'a' or x2 > 'h':
            print("Columns are between A and H")
            continue

        break
    return(move)

while True:
    display_board(bd, piece_arr)

    move = get_command()
    os.system('cls' if os.name == 'nt' else 'clear')


    start_x = ord(move[0]) - ord('a')
    start_y = int(move[1]) - 1
    end_x = ord(move[2]) - ord('a')
    end_y = int(move[3]) - 1

    start_pos = (start_x, start_y)
    end_pos = (end_x, end_y)

    for piece in piece_arr:
        if piece[0] == start_x and piece[1] == start_y: # checks if a piece is on start square
            if is_square_free(end_x, end_y, piece_arr, piece):  # checks if the end square is free
                if is_way_free(start_pos, end_pos, piece_arr) or piece[2] == "♘" : #checks if trajectory is free or piece = k
                    if what_trajectory(start_pos, end_pos)[0] in piece[3] and what_trajectory(start_pos, end_pos)[1] <= piece[4]:
                        if piece[2] == "♙":
                            if end_y > start_y:
                                piece[0] = end_x
                                piece[1] = end_y
                                piece[4] = 1
                                print(piece)
                                if end_y == 7:
                                    piece_arr.remove(piece)
                                    piece = [end_x, end_y, "♕", ["h", "v", "d"], 7, 1]
                                    piece_arr.append(piece)
                                    print(piece)
                            else:
                                break
                        if piece[2] == "♟":
                            if end_y < start_y:
                                piece[0] = end_x
                                piece[1] = end_y
                                piece[4] = 1
                                if end_y == 0:
                                    piece_arr.remove(piece)
                                    piece = [end_x, end_y, "♛", ["h", "v", "d"], 7, 2]
                                    piece_arr.append(piece)
                            else:
                                break
                        piece[0] = end_x
                        piece[1] = end_y
                    else:
                        print("that piece does not move like that, or that far")
            else:
                print("square not free")
    print(f"White cemetery: {' '.join(dead_white_pieces)}\nBlack cemetery: {' '.join(dead_black_pieces)}")

