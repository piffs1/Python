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
for i in myCat.values():
	print(i, end=" ")
print()
print("=======================")
print("myCat.keys is ", end=" ")
for i in myCat.keys():
	print(i, end=" ")
print()
print("=======================")
for i in myCat.items():
	print(i)
	print(type(i))
print(myCat.keys())
print(myCat)
print(pprint.pformat(myCat))