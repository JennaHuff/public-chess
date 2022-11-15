def place_pieces(arr):
    pawns(arr)
    queens(arr)
    rooks(arr)
    knights(arr)
    bishops(arr)
    kings(arr)

def pawns(arr):
    
    w_y, b_y = 1, 6

    for w_x in range(8):
        wp = [w_x, w_y, "♙", ["v"], 2, 1] # 2 = range, 1 = white
        arr.append(wp)

    for b_x in range(8):
        bp = [b_x, b_y, "♟", ["v"], 2, 2]
        arr.append(bp)

def rooks(arr):

    wr = [0, 0, "♖", ["h", "v"], 7, 1]
    wr2 = [7, 0, "♖", ["h", "v"], 7, 1]
    br = [0, 7, "♜", ["h", "v"], 7, 2]
    br2 = [7, 7, "♜", ["h", "v"], 7, 2]
    arr.append(wr)
    arr.append(wr2)
    arr.append(br)
    arr.append(br2)

def knights(arr):

    wk = [1, 0, "♘", ["k"], 1, 1]
    wk2 = [6, 0, "♘", ["k"], 1, 1]
    bk = [1, 7, "♞", ["k"], 1, 2]
    bk2 = [6, 7, "♞", ["k","v"], 1, 2]
    arr.append(wk)
    arr.append(wk2)
    arr.append(bk)
    arr.append(bk2)

def bishops(arr):

    wb = [2, 0, "♗", ["d"], 7, 1]
    wb2 = [5, 0, "♗", ["d"], 7, 1]
    bb = [2, 7, "♝", ["d"], 7, 2]
    bb2 = [5, 7, "♝", ["d"], 7, 2]
    arr.append(wb)
    arr.append(wb2)
    arr.append(bb)
    arr.append(bb2)

def queens(arr):
    wq = [3, 0, "♕", ["h", "v", "d"], 7, 1]
    bq = [3, 7, "♛", ["h", "v", "d"], 7, 2]
    arr.append(wq)
    arr.append(bq)

def kings(arr):
    wk = [4, 0, "♔", ["h", "v", "d"], 1, 1]
    bk = [4, 7, "♚", ["h", "v", "d"], 1, 2]
    arr.append(wk)
    arr.append(bk)