def checkmate(board: str):
    """
    Takes a chessboard as a string and checks if the King is in check.
    Prints "Success" if in check, otherwise "Fail".
    """

    # Turn board string into 2D list
    rows = [list(row) for row in board.strip().split("\n")]
    n = len(rows)

    # Find the King
    king_pos = None
    for i in range(n):
        for j in range(len(rows[i])):
            if rows[i][j] == "K":
                king_pos = (i, j)
                break
    if not king_pos:
        print("Error")  # no King found
        return

    kx, ky = king_pos


    # ---------------- Pawns ----------------
    # Pawns capture diagonally one step up
    for i in range(n):
        for j in range(len(rows[i])):
            if rows[i][j] == "P":
                if (i-1, j-1) == (kx, ky) or (i-1, j+1) == (kx, ky):
                    print("Success")
                    return

    # ---------------- Rooks ----------------
    # Rook moves: up, down, left, right
    directions_rook = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in directions_rook:
        x, y = kx+dx, ky+dy
        while 0 <= x < n and 0 <= y < len(rows[x]):
            piece = rows[x][y]
            if piece != ".":        # first piece in this direction
                if piece == "R":    # rook attacks
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # ---------------- Bishops ----------------
    # Bishop moves: diagonals
    directions_bishop = [(1,1), (1,-1), (-1,1), (-1,-1)]
    for dx, dy in directions_bishop:
        x, y = kx+dx, ky+dy
        while 0 <= x < n and 0 <= y < len(rows[x]):
            piece = rows[x][y]
            if piece != ".":
                if piece == "B":    # bishop attacks
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # ---------------- Queens ----------------
    # Queen = Rook + Bishop moves
    directions_queen = directions_rook + directions_bishop
    for dx, dy in directions_queen:
        x, y = kx+dx, ky+dy
        while 0 <= x < n and 0 <= y < len(rows[x]):
            piece = rows[x][y]
            if piece != ".":
                if piece == "Q":    # queen attacks
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # ---------------- If nothing found ----------------
    print("Fail")
