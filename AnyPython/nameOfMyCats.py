petNames = []
while True:
	name = input("Моего питомца зовут ")
	if(name == ""):
		break
	petNames = petNames + [name]
print("Моих питомцев зовут :")
for name in petNames: #foreach analog
	print(name)
if "Собакен" not in petNames:
	print("Ты забыл Собакена!")
if "Кошакен" not in petNames:
	print("Ты забыл Кошакена!")
if "Боря" not in petNames:
	print("Ты забыл Борю!")
if "Попугакен" in petNames:
	print("Все впорядке, Попугакена ты не забыл!")
print ("Попугакен" in petNames)