grid = [[".","C",".",".",".","."],
		["D",".",".",".",".","C"],
		[".",".",".",".",".","."],
		[".",".",".",".",".","."],
		[".",".",".",".",".","."],
		[".",".",".",".",".","."],
		[".",".",".",".",".","."],
		[".",".",".",".",".","."],
		[".",".",".",".",".","."]]

#for i in range(len(grid)):
#	print(len(grid[i]))
#print("grid[",len(grid),"][",len(grid[0]),"]", sep="")
for i in range(len(grid)):
	for j in range(len(grid[i])):
		grid[i][j] = "."
grid[0] = grid[len(grid)-1]
grid[1][1] = grid[1][2] = "O"
grid[len(grid)-2] = grid[1]
for i in range(4):
	grid[2][i] = "O"
grid[len(grid)-3] = grid[2]
for i in range(5):
	grid[3][i] = "O"
grid[len(grid)-4] = grid[3]
for i in range(1, len(grid[0])):
	grid[4][i] = "O"
for j in range(len(grid[0])):
	for i in range(len(grid)):
		print(grid[i][j], end="")
	print()