def findFromDictionary(param):
	global myDic
	if param in myDic: # EQUAL param in spam.keys()
		print("myDic[" + str(param) + "] = " + myDic[param])
	else:
		print("myDic[" + str(param) + "] не найден, " +
			"возможно поискать в значениях ?(y/n) ")
		inp = input()
		flag = False
		if (inp=="y"):
			for key,value in myDic.items():
				try:
					if(value == int(param)):
						print("Значение " + param +" соответствует ключу " + key)
						flag = True
				except ValueError:
					if(value == param):
						print("Значение " + param +" соответствует ключу " + key)
		if(not flag):
			print("Значение не найдено!")

			

spam = {"color" : "red", "age" : 42}

for k,v in spam.items():
	print("Key: " + k + " value: " + str(v))

for lst in spam.items():
	print("Key: " + lst[0] + " value: " + str(lst[1]))

myDic = {"cat" : "cool", "dog" : "strong", "weight" : "hue", "age" : 42}
while True:
	inp = input("Поиск по : ")
	if(inp==""):
		break
	findFromDictionary(inp)