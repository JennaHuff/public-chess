"""
This function deconstructs an input and returns its parts in a dictionary

Example:
user_input = fxg8=Q#
returns:
{'letter': 'f', 'coordinate': 'g8', 'specialFx': '=Q#', 'capture': True, 'check': False}

This function fails to account for:
    --multiple-coordinate-moves such as "Nd1xc3+"
(https://lichess.org/editor/8/8/1R6/3N4/5K2/2q5/kB6/1N1N4_w_-_-_0_1?color=white)
    --numbers-only moves
    --does not check if the piece letter corresponds to a piece
    --the piece can be "aaaaaaaaah what a poorly written function", if followed by coordinates
    --does not check if the coordinates exist
"""


def analyse_move(user_input):
    part = 0
    i = 0
    while i < len(user_input):
        if user_input[i].isdigit():
            part = user_input.partition(user_input[i - 1] + user_input[i])
            break
        i += 1
    #  part == ('Rax', 'b5', '+#'), b5 being user_input[i] and user_input[i -1]
    if part == 0:
        raise TypeError("invalid input")
    deconstructed_input = {
        "letter": part[0].replace("x", ""),
        "coordinate": part[1],
        "specialFx": part[2],
        "capture": "x" in part[0],
        "check": "+" in part[2]
                  }
    if deconstructed_input["letter"] == '':
        deconstructed_input["letter"] = 'P'                             # this must be a pawn
    return deconstructed_input

