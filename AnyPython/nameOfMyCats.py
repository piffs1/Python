petNames = []
while True:
	name = input("Моего питомца зовут ")
	if(name == ""):
		break
	petNames = petNames + [name]
print("Моих питомцев зовут :")
for name in petNames: #foreach analog
	print(name)
if "Дуся" not in petNames:
	print("Ты забыл Дусю!")
if "Лео" not in petNames:
	print("Ты забыл Лео!")
if "Боря" not in petNames:
	print("Ты забыл Борю!")
if "Тоша" in petNames:
	print("Все впорядке, Тошу ты не забыл!")
print ("Тоша" in petNames)