def printTable(param):
	colWidths = [0] * len(param)
	for i in range(len(param)):
		for j in range(len(param[i])):
			if(colWidths[i] < len(param[i][j])):
				colWidths[i] = len(param[i][j])
	for i in range(len(param[0])):
		for j in range(len(param)):
			print(param[j][i].rjust(colWidths[j]),end = " ")
		print()
tableData = [["apples","oranges","cherries","banana"],
			["Alice","Bob","Carol","David"],
			["Dogs","Cats","Moose","Goose"]]
printTable(tableData)