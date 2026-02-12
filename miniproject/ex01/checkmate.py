def checkPos(grid: list, text: str):
    size = len(grid)
    amount = 0
    cord = []
    for row in range(size):
        for col in range(len(grid[row])):
            if grid[row][col] == text:
                amount += 1
                cord.append((row, col))
    return cord or None, amount 
    
def checkSquare(grid: list) -> bool:
    for row in grid:
        if len(row) != len(grid):
            return False
    return True

def walk(grid,row,col,dr,dc,kr,kc):
    size = len(grid)

    r = row + dr
    c = col + dc

    while 0 <= r < size and 0 <= c < size:
        if r == kr and c == kc:
            return True
        if grid[r][c] != ".":
            return False
        
        r += dr
        c += dc

    return False

def canAttack(grid, piece, pr, pc, kr, kc):
    if piece == "P":
        return kr == pr - 1 and abs(kc - pc) == 1
    
    if piece == "B":
        directions = [(1,1),(1,-1),(-1,1),(-1,-1)]
        for dr,dc in directions:
            if walk(grid,pr,pc,dr,dc,kr,kc):
                return True
        return False

    if piece == "R":
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for dr,dc in directions:
            if walk(grid,pr,pc,dr,dc,kr,kc):
                return True
        return False

    if piece == "Q":
        directions = [
            (1,0),(-1,0),(0,1),(0,-1),
            (1,1),(1,-1),(-1,1),(-1,-1)
        ]
        for dr,dc in directions:
            if walk(grid,pr,pc,dr,dc,kr,kc):
                return True
        return False

def checkmate(board):
    grid = [list(row) for row in board.split()]
    size = len(grid)
    # print(grid, size)
    if not checkSquare(grid): print("Board is not square"); return False, "Board is not square"

    King, KAmount = checkPos(grid, "K")
    Pawn, PAmount = checkPos(grid, "P")
    Bishop, BAmount = checkPos(grid, "B")
    Rook, RAmount = checkPos(grid, "R")
    Queen, QAmount = checkPos(grid, "Q")
    
    if KAmount > 1 or KAmount < 1:
        return False, "Error King Not Found" 

    pieces = [("P", Pawn), ("B", Bishop), ("R", Rook), ("Q", Queen)]
    kr, kc = King[0] or None
    for pieceName, pos in pieces:
        if pos is not None:
            for (pr, pc) in pos:
                if canAttack(grid, pieceName, pr, pc, kr, kc):
                    print("Success")
                    return
    print("Fail")
"""
[
    K = 1, 1
    R = 0, 0
    P = 2, 2
    ['R', '.', '.', '.'], 
    ['.', 'K', '.', '.'], 
    ['.', '.', 'P', '.'], 
    ['.', '.', '.', '.']] 

"""