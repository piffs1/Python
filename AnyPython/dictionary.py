import pprint

myCat = {"size" : "fat", "color" : "gray" , 
"disposition" : "loud" , 12 : "red"}
myDog = {"size" : "fat", 12 : "red", "color" : "gray", "disposition" : "loud"}
prop = input("Качество котика ")
if prop in myCat:
	print("Качество " + prop + " есть у котика!")
else:
	print("Такого качества у котика нет !")
print("=======================")
print("myCat.values is ", end=" ")
for i in myCat.values(): # Поиск по значениям
	print(i, end=" ")
print()
print("=======================")
print("myCat.keys is ", end=" ")
for i in myCat.keys():	# Поиск по ключам
	print(i, end=" ")
print()
print("=======================")
for i in myCat.items(): # Поиск по ключу-значению 
	print(i)
	print(type(i))		# tuple
print(myCat.keys())		# dict_keys(myCat)
print(myCat)
print(pprint.pformat(myCat))