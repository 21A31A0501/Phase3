'''
#(0,0)---->(8,8)
def printMatrix(x, y, board):
    if x == 9:
        print("Traversal completed")
        return 
 
    print(board[x][y], end = " ")
    nextX, nextY = -1, -1 
 
    if y == 8:
        nextX = x + 1 
        nextY = 0 
        print()
    else:
        nextX = x 
        nextY = y + 1
 
    printMatrix(nextX, nextY, board)
 
board = []
for i in range(9):
    row = []
    for j in range(1, 10):
        row.append(j)
    board.append(row)
printMatrix(0, 0, board)
'''


#(8,8)--->(0,0)
def printMatrix(x, y, board):
    if x ==-1:
        print("Traversal completed")
        return 
 
    print(board[x][y], end = " ")
    nextX, nextY = N-1, N-1 
 
    if y == 8:
        nextX = x -1
        nextY = y
        print()
    else:
        nextX = x 
        nextY = y -1
 
    printMatrix(nextX, nextY, board)
board = []
N=len(board)
for i in range(9):
    row = []
    for j in range(10,-1,1):
        row.append(j)
    board.append(row)
printMatrix(0, 0, board)