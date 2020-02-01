## Backtracking famous problems


# def permute(s, chosen = [], alreadyPrinted= {}):

# 	if( not len(s)):

# 		if(''.join(chosen) in alreadyPrinted):
# 			pass
# 		else:
# 			print(''.join(chosen))
# 			alreadyPrinted[''.join(chosen)]=1
# 		return

		
# 	else:
# 		# choose , explore and unchoose char

# 		for i in range(len(s)):

# 			charChosen = s[i]  # choose
# 			chosen.append(charChosen)
# 			del s[i]


# 			permute(s, chosen, alreadyPrinted) # explore


# 			s.insert(i, charChosen)  # Un-choose
# 			chosen.pop()


# permute(list('google'))





# Q2 N-Queen problems


# def isSafe(board, row, col):
# 	for val in board[row]:          #row
# 		if val==1:
# 			return False

# 	for i in range(len(board)):		#col
# 		if board[i][col]==1:
# 			return False


# 	currRow = row
# 	currCol = col
# 	while(True):					#upper diagonal Right
# 		if(board[currRow][currCol]==1):
# 			return False
# 		else:
# 			currRow = currRow-1
# 			currCol = currCol+1

# 			if(currRow>=0 and currRow<len(board) and currCol>=0 and currCol<len(board)):
# 				pass
# 			else:
# 				break

# 	currRow = row
# 	currCol = col      
# 	while(True):					#lower diagonal left
# 		if(board[currRow][currCol]==1):
# 			return False
# 		else:
# 			currRow = currRow+1
# 			currCol = currCol-1

# 			if(currRow>=0 and currRow<len(board) and currCol>=0 and currCol<len(board)):
# 				pass
# 			else:
# 				break

# 	currRow = row
# 	currCol = col
# 	while(True):					#lower diagonal right
# 		if(board[currRow][currCol]==1):
# 			return False
# 		else:
# 			currRow  = currRow+1
# 			currCol = currCol+1
# 			if(currRow>=0 and currRow<len(board) and currCol>=0 and currCol<len(board)):
# 				pass
# 			else:
# 				break



# 	currRow = row
# 	currCol = col
# 	while(True):					#upper diagonal left
# 		if(board[currRow][currCol]==1):
# 			return False
# 		else:
# 			currRow  = currRow-1
# 			currCol = currCol-1
# 			if(currRow>=0 and currRow<len(board) and currCol>=0 and currCol<len(board)):
# 				pass
# 			else:
# 				break




# 	return True





# def saveQueens(n, board, saved=0):

# 	if n==0:
# 		for row in board:
# 			print(*row)


# 		print('------------------')
# 		print()
# 		print()
# 		return
# 	else:
# 		for i in range(len(board)):
# 			if isSafe(board, saved, i):
				
# 				board[saved][i] = 1
# 				saved+=1
				
# 				saveQueens(n-1, board, saved)

# 				saved-=1
# 				board[saved][i] = 0
				

# 			else:
# 				pass
# 		return


# def NQueens(n):
# 	board = []
# 	for i in range(n):
# 		data = [0]*n
# 		board.append(data)

# 	saveQueens(n, board)

# NQueens(5)



# Q3 sum of subset problem


# def sumOfSubset(arr, m, subset = []):

# 	if sum(subset)==m:
# 		print(*subset)
# 		return

# 	if sum(subset)>m:
# 		return

# 	else:

# 		for i in range(len(arr)):

# 			val = arr[i]
# 			subset.append(val)
# 			del arr[i]

# 			sumOfSubset(arr, m, subset)

# 			subset.pop()
# 			arr.insert(i, val)


# sumOfSubset([5, 10, 12, 13, 15, 18], 30)




#  Q4 Print all possible paths from top left to bottom right of a mXn matrix


# def AllPossiblePaths(board, rows, cols, path = [1], current = [0,0]):

# 	if(current == [rows-1, cols-1]):
# 		print(*path)
# 		return

# 	else:

# 		if(current[1]+1<cols):
# 			current[1]+=1
# 			path.append(board[current[0]][current[1]])

# 			AllPossiblePaths(board, rows, cols, path, current)

# 			current[1]-=1
# 			path.pop()

# 		if(current[0]+1<rows):
# 			current[0]+=1
# 			path.append(board[current[0]][current[1]])

# 			AllPossiblePaths(board, rows, cols, path, current)
# 			current[0]-=1
# 			path.pop()


# 		return

# AllPossiblePaths([[1,2,3], [4,5,6]], 2, 3)



#  Q5 Rat in a maze

# def ratInMaze(maze, path, current = [0,0]):

# 	if(current == [len(maze)-1, len(maze)-1]):
# 		for row in path:
# 			print(*row)
# 		print('--------------')
# 		print()

# 		return
# 	else:

# 		if(current[1]+1<len(maze) and maze[current[0]][current[1]+1]!=0):
# 			current[1]+=1
# 			path[current[0]][current[1]] = 1

# 			ratInMaze(maze, path, current)

# 			path[current[0]][current[1]] = 0
# 			current[1]-=1

# 		if(current[0]+1<len(maze) and maze[current[0]+1][current[1]]!=0):
# 			current[0]+=1
# 			path[current[0]][current[1]] = 1

# 			ratInMaze(maze, path, current)

# 			path[current[0]][current[1]] = 0
# 			current[0]-=1

# 		return


# ratInMaze([[1,0,0,0,0], [1,1,1,0,0], [1,1,1,0,0], [1,1,1,0,0], [1,1,1,1,1]], [[1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])



# Q6 Sudoku solver




# def isEmpty(board):
# 	for row in board:
# 		for val in row:
# 			if val==0:
# 				return True

# 	return False


# def getEmptyPos(board):
# 	for i in range(len(board)):
# 		for j in range(len(board)):
# 			if board[i][j]==0:
# 				return (i, j)

# 	return False




# def isSafe(board, row, col, val):

# 	for num in board[row]:    # same row
# 		if num==val:
# 			return False

# 	for i in range(len(board)):   #same col
# 		if board[i][col]==val:
# 			return False

# 	rowRem = row%3
# 	colRem = col%3
# 	gridRow = row - rowRem
# 	gridCol = col - colRem
# 	startGridRow = gridRow
# 	startGridCol = gridCol


# 	for i in range(3):			#same 3X3 grid
# 		gridCol = startGridCol
# 		for j in range(3):
# 			if board[gridRow][gridCol] == val:
# 				return False

# 			gridCol+=1

# 		gridRow+=1


# 	return True




# def sudoku(board):

# 	if(not isEmpty(board)):
# 		for row in board:
# 			print(*row)

# 		print('------------------------')
# 		print()
# 		return

# 	else:
# 		pos = getEmptyPos(board)
# 		row = pos[0]
# 		col = pos[1]

# 		for i in range(1, 10):

# 			if isSafe(board, row, col, i):
# 				board[row][col] = i

# 				sudoku(board)

# 				board[row][col] = 0
# 	return


# sudoku([
# 	   [3,0,6,5,0,8,4,0,0],
# 	   [5,2,0,0,0,0,0,0,0], 
# 	   [0,8,7,0,0,0,0,3,1],
# 	   [0,0,3,0,1,0,0,8,0],
# 	   [9,0,0,8,6,3,0,0,5],
# 	   [0,5,0,0,9,0,6,0,0],
# 	   [1,3,0,0,0,0,2,5,0],
# 	   [0,0,0,0,0,0,0,7,4],
# 	   [0,0,5,2,0,6,3,0,0]])





#  Q7 Generate all possible matched paranthesis

count = 0
def allPossibleParHelper(n, size, s=[], opening=0, closing=0):
	global count
	if n<0:
		return

	if (len(s)==size) and (opening==size//2) and (closing==size//2):
		count+=1
		print(''.join(s))
		return

	if closing>opening:
		return

	if opening>size//2:
		return

	if closing>size//2:
		return


	s.append('(')   #Choose
	opening+=1

	allPossibleParHelper(n-1, size, s, opening, closing)   # Explore

	s.pop()         # Dechoose
	opening-=1





	s.append(')')   #Choose
	closing+=1

	allPossibleParHelper(n-1, size, s, opening, closing)   #Explore

	s.pop()     #Dechoose
	closing-=1




def allPossiblePar(n):
	allPossibleParHelper(n, size=n)
	


allPossiblePar(6)
print(count)























