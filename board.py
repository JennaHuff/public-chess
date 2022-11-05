import math
#import NewPiece


# two attempts at creating a board: a dictionary with 64 entries, and an 8x8 2d array


# creates a "board" dictionary, with str coordinates as keys and 1-64 ints as values
# 1: a1, 8: h1, 63: g8, 64: h8
def create_dict_board():
    board = {}
    i = 1
    while i < 65:
        number = int(math.ceil(i / 8))
        letter = chr(ord('h') - int(number * 8 - i))
        board[f"{letter}{number}"] = f"{i}"
        i += 1
    return board


# instantiates Square objects and stores them as values to every key in dict
def fill_with_squares(dictionary):
    for i in dictionary:
        dictionary[i] = NewPiece.Square(i, None, False, False)
    return dictionary


def display_board(dictionary):
    board = []
    for j in range(8):
        column = []
        for i in range(8):
            print(i, j)
            column.append('')
        board.append(column)
    return board


def create():               # creates an 8x8 2d array
    board = []
    for j in range(8):
        column = []
        for i in range(8):
            column.append(' ')
        board.append(column)
    return board


def display(two_d_list):    # if board is a 2D array
    two_d_list.reverse()
    for columns in two_d_list:
        print(columns)
    two_d_list.reverse()
