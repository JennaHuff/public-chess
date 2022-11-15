import copy
import os
import place_piece
import how_far



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

def count_score(arr):
    score = 0

    for piece in arr:
        if piece == "♙" or piece == "♟":
            score += 1
        if piece == "♖" or piece == "♜":
            score += 5            
        if piece == "♘" or piece == "♞":
            score += 3
        if piece == "♗" or piece == "♝":
            score += 3
        if piece == "♕" or piece == "♛":
            score += 9

    return score

def compare_scores(num_1, num_2):
    if num_1 == num_2:
        return f"  ", f"  "
    if num_1 > num_2:
        return f"+{num_1 - num_2}", "  "
    else:
        return "  ", f"+{num_2 - num_1}"


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
    if how_far.horizontaly(start_pos, end_pos):
        return ("h", how_far.horizontaly(start_pos, end_pos))
    if how_far.verticaly(start_pos, end_pos):
        return ("v", how_far.verticaly(start_pos, end_pos))
    if how_far.diagonaly(start_pos, end_pos):
        return ("d", how_far.diagonaly(start_pos, end_pos))
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
            if how_far.diagonaly(piece_coords, start_pos) and how_far.diagonaly(piece_coords, end_pos) and piece[0] > smallest_x and piece[0] < biggest_x:
                print("diagonal not free")
                print(f"piece captures {piece[2]}")
                return 0
        return 1


def get_command(): # Checks for conformity of user input with expected args
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


bd = create_board()

piece_arr = []
place_piece.place_pieces(piece_arr)


while True:
    w_score = count_score(dead_white_pieces)
    b_score = count_score(dead_black_pieces)
    score = compare_scores(w_score, b_score)
    print(f"{score[0]} Captured white pieces: {' '.join(dead_white_pieces)}")

    display_board(bd, piece_arr)

    print(f"{score[1]} Captured black pieces: {' '.join(dead_black_pieces)}")

    move = get_command()
    os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal before displaying board again


    start_x = ord(move[0]) - ord('a')                # ex: h8h1 --> 7 7 7 0
    start_y = int(move[1]) - 1
    end_x = ord(move[2]) - ord('a')
    end_y = int(move[3]) - 1

    start_pos = (start_x, start_y)                   # (7, 7)
    end_pos = (end_x, end_y)                         # (7, 0)


    for piece in piece_arr:
        if not (piece[0] == start_x and piece[1] == start_y): # if the piece is not on start square
            continue                                          # it won't be the one we want to move
        if not(is_way_free(start_pos, end_pos, piece_arr) or piece[2] == "♘" or piece[2] == "♞"):
            continue                                          # if trajectory is not free and piece is not knight

        # Compares piece's allowed movements, to kind of trajectory
        if not (what_trajectory(start_pos, end_pos)[0] in piece[3] and what_trajectory(start_pos, end_pos)[1] <= piece[4]):
            print("that piece does not move like that, or that far")
            continue

        if not (is_square_free(end_x, end_y, piece_arr, piece)):  # checks if the end square is free
            continue

        if piece[2] == "♙":
            if end_y > start_y:                 # White pawns can only move downwards
                piece[0] = end_x
                piece[1] = end_y
                piece[4] = 1                    # Pawns can move 2 squares on first move only, range then becomes 1
                if end_y == 7:                  # Promotion!
                    piece_arr.remove(piece)
                    piece = [end_x, end_y, "♕", ["h", "v", "d"], 7, 1]
                    piece_arr.append(piece)

        if piece[2] == "♟":
            if end_y < start_y:                 # Black pawns can only move downwards
                piece[0] = end_x
                piece[1] = end_y
                piece[4] = 1                    # Pawns can move 2 squares on first move only, range then becomes 1
                if end_y == 0:                  # Promotion!
                    piece_arr.remove(piece)
                    piece = [end_x, end_y, "♛", ["h", "v", "d"], 7, 2]
                    piece_arr.append(piece)

        piece[0] = end_x                        # If all the conditions match, move the piece
        piece[1] = end_y


    

