# public-chess

To do:

pawns can take vertically

pawns can only promote to queens

scores should count the difference between total pieces, not just taken pieces

when prompted to pick a piece to promote to, input is not guarded

a king in check should blink red
cannot move any piece when in check, unless the piece is the king or the piece

players should take turns playing
handle inputs such as "Nd1xc3", or "e4"

# def is_free_or_can_take(x, y, arr, moving_piece):
#     for piece in arr:
#         if piece[0] == x and piece[1] == y:         #   Checks if the piece is on the destination square
#             if piece[5] != moving_piece[5]:         #   Checks if the piece is of the same color
#                 print(f"{moving_piece[2]} takes {piece[2]}")
#                 if piece[5] == 1:                   # 1 == white
#                     dead_white_pieces.append(piece[2])
#                 else:
#                     dead_black_pieces.append(piece[2])
#                 arr.remove(piece)
#                 return 1
#             return 0
#     return 1

# def is_free_or_can_take(x, y, arr, moving_piece):  # 0 == occupied, 1 == free, 2 == take-able
#     for piece in arr:
#         if piece[0] == x and piece[1] == y:         #   Checks if the piece is on the destination square
#             if piece[5] != moving_piece[5]:         #   Checks if the piece is of the same color
#                 print(f"{moving_piece[2]} takes {piece[2]}")
#                 if piece[5] == 1:                   # 1 == white
#                     dead_white_pieces.append(piece[2])
#                 else:
#                     dead_black_pieces.append(piece[2])
#                 return 2                            # piece occupies the square but can be taken
#             else:
#                 return 0
#     return 1