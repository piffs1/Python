spam = [] # присвоено списковое значение
print(spam) # []
spam1 = [1, 1.0, "1"]
print(len(spam1)) # 3
for i in range(len(spam1)):
	print(spam1[i])
try:
	print(spam1[float(10)])
except IndexError: #OUT OF RANGE
	print("12w3")
except:
	print("=(") # out this
print(["cat","bat","elephant"][0]) # cat
bam = [["cat","dog","some animal"], [10,13,16]]
print(bam[0][1]) # dog
vam = [[["cat","dog"],[1,2,3]],[["rat","mice"],[3,4,5]]] # Сначала раскрываются двойные скобки, потом одинарные, потом само значение
print(vam)
print(vam[0][1][1]) #2
print(vam[1][0][0]) #rat
print(vam[1][1][2]) #5
bes = ["cat","dogs","rogs"]
print(bes[-1]) # rogs
# print(bes[-3]) # out of range
print(bes[0:1]) # 0 includes, 1 not includes
print(bes[0:2])
print(bes[:2]) #bes[0],bes[1]
print(bes[1:]) #bes[1] #bes[2]
print(bes[:]) # all
print(bes[0:-2]) # просто указывает на len(bes)-2 элемент. По сути [0:1]
print("CONCANTENATION?")
print([1,2,3] + ["A","B","C"]) # [1,2,3, "A", "B", "C"]
print([1,2,3] * 3) # [1,2,3,1,2,3,1,2,3]
print("DELETING")
spam = ["cat","bat","rat"]
print(spam)
del spam[2] # для удаление значений из списков
print(spam) # cat,bat
print("SEARCH FROM INDEX")
try:
	print(spam.index("cat1")) # В случае повторов возвращается первое значение
except ValueError:
	print("Элемента не найдено")
print("OLD LIST ", spam)
spam.append("boose") # push_back
spam.insert(-1, "2007") # Если выход за границу, то добавляет либо в конец, либо в начало
print("NEW LIST ", spam)
spam.remove("2007") #OK. В худшем случае вызывается exception ValueError
# del подходит, когда мы точно знаем индекс del spam[0] к примеру.
# list.remove удаляет первый элемент который встретит в листе
print(spam)
spam = [2,4,5,1,0, 3.12, 3.128]
spam.sort(reverse=True)
print(spam) #OK reverse sort
spam = ["a","z","A","Z"]
spam.sort(key=str.lower)
print(spam) # [a,A,z,Z]