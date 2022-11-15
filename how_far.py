def horizontaly(start_pos, end_pos):
    if start_pos[1] == end_pos[1]:
        nb_of_steps = abs(start_pos[0] - end_pos[0])
        return nb_of_steps
    else:
        return 0

def verticaly(start_pos, end_pos):
    if end_pos[0] == start_pos[0]:
        nb_of_steps = abs(start_pos[1] - end_pos[1])
        return nb_of_steps
    else:
        return 0

def diagonaly(start_pos, end_pos):
    x_compare = abs(start_pos[0] - end_pos[0])
    y_compare = abs(start_pos[1] - end_pos[1])
    if x_compare == y_compare:
        nb_of_steps = x_compare
        return nb_of_steps
    else:
        return 0