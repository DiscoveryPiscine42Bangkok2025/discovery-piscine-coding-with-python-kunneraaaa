def checkmate(board: str):

    rows = [list(row) for row in board.strip().split("\n")] #แถว
    n = len(rows) #คอลลัม

    # King
    king_pos = None
    for i in range(n):
        for j in range(len(rows[i])):
            if rows[i][j] == "K":
                king_pos = (i, j)
                break
    if not king_pos:
        print("Error")  
        return

    kx, ky = king_pos


    # Pawns
    for i in range(n):
        for j in range(len(rows[i])):
            if rows[i][j] == "P":
                if (i-1, j-1) == (kx, ky) or (i-1, j+1) == (kx, ky):
                    print("Success")
                    return

    # Rooks
    directions_rook = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in directions_rook:
        x, y = kx+dx, ky+dy
        while 0 <= x < n and 0 <= y < len(rows[x]):
            piece = rows[x][y]
            if piece != ".":        
                if piece == "R":    
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # Bishops
    directions_bishop = [(1,1), (1,-1), (-1,1), (-1,-1)]
    for dx, dy in directions_bishop:
        x, y = kx+dx, ky+dy
        while 0 <= x < n and 0 <= y < len(rows[x]):
            piece = rows[x][y]
            if piece != ".":
                if piece == "B":    
                    print("Success")
                    return
                break
            x += dx
            y += dy

    # Queens

    directions_queen = directions_rook + directions_bishop
    for dx, dy in directions_queen:
        x, y = kx+dx, ky+dy
        while 0 <= x < n and 0 <= y < len(rows[x]):
            piece = rows[x][y]
            if piece != ".":
                if piece == "Q":    
                    print("Success")
                    return
                break
            x += dx
            y += dy

    print("Fail")
