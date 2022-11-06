import math


def get_coordinate(index):
    number = math.ceil(index / 8)
    letter = chr(ord('a') + index % 8)

    coordinate = letter + str(number)
    return coordinate


print(get_coordinate(0))


def get_index(coordinate):
    number = (8 * int(coordinate[1])) - (int(ord('h')) - int(ord(coordinate[0])))
    return number
    # print(number)


#print(get_coordinate(8))    # prints "h1"
#print(get_index("h1"))      # prints 8
