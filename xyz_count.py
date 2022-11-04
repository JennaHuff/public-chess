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
