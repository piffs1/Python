birthdays = {"Alice" : "Apr 1", "Bob" : "Dec 12",
"Carol" : "Mar 4"}
while True:
	name = input("Введите имя : ")
	if name == "":
		break
	if name in birthdays:
		print("У " + name + " день рождения " + birthdays[name])
	else:
		print("Имени " + name + " не существует")
		bday = input("Когда у него Д/Р ? ")
		birthdays[name] = bday
		print("База данных обновлена")
