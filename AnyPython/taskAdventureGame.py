def displayInventory(a_inventory):
	print("Inventory:")
	nCount = 0
	for item in a_inventory.items():
		print(str(item[1]) + " " + item[0])
		nCount = nCount + item[1]
	print("Total number of items : " + str(nCount))
displayInventory({"arrow" : 12, "poison" : 1})