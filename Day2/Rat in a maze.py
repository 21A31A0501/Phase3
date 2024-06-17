#Rat in a maze---leetcode
'''
D-down
U-up
L-left 
R-right
  
4*4 matrix
00 01 02 03
10 11 12 13
20 21 22 23
30 31 32 33

(0,0)--->(3,3)
(top_leftcordinates)-->(bottom-right cordinates)

Current cordinates of rat is : (2,1)  (x,y)
top:(1,1)  (x-1,y)
bottom:(3,1)  (x+1,y)
left:(2,0)  (x,y-1)
right:(2,2)  (x.y+1)

Current cordinates : (x,y)
top:(x-1,y)
bottom:(x+1,y)
left:(x,y-1)
right:(x,y+1)

(should not go to negative values and should not cross n-1)
4-directionally adjacent coordinates
'''


def findAllWays(x, y, matrix, N, path, visited):
	# Border checks
	if x < 0 or x == N or y < 0 or y == N:
		return
 
	# Condition to check whether we can traverse via those coordinates or not
	if matrix[x][y] == 0 or visited[x][y] == True:
		return
 
	# Condition to check whether we've reached our final coordinates or not
	if x == N - 1 and y == N - 1:
		print("".join(path))
		return
 
	visited[x][y] = True 
 
	# Top Direction
	path.append("U")
	findAllWays(x - 1, y, matrix, N, path, visited)
	path.pop()
 
	# Bottom Direction
	path.append("D")
	findAllWays(x + 1, y, matrix, N, path, visited)
	path.pop()
 
	# Left Direction 
	path.append("L")
	findAllWays(x, y - 1, matrix, N, path, visited)
	path.pop()
 
	# Right Direction
	path.append("R")
	findAllWays(x, y + 1, matrix, N, path, visited)
	path.pop()
	visited[x][y]=False
 
 
path = []
visited = []
matrix = [[1, 1, 0, 0], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
n = len(matrix)
 
for i in range(n):
	eachRow = []
	for j in range(n):
		eachRow.append(False)
	visited.append(eachRow)
findAllWays(0, 0, matrix, n, path, visited)