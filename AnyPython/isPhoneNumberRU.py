def isPhoneNumber(text):
	if (len(text) != 15):
		return False
	if not text[0].isdecimal():
		return False
	if text[1] != "-":
		return False
	for i in range(2,5):
		if not text[i].isdecimal():
			return False
	if text[5] != "-":
		return False
	for i in range(6,9):
		if not text[i].isdecimal():
			return False
	if text[9] != "-":
		return False
	for i in range(10,12):
		if not text[i].isdecimal():
			return False
	if text[12] != "-":
		return False
	for i in range(13,15):
		if not text[i].isdecimal():
			return False
	return True

message = "Меня зовут Бориска, я настоящий котенок у меня два телефона. Первый : 8-912-623-92-01 и второй для друзей 8-274-012-99-48"
print(message)
nCountNumbers = 0
for i in range(len(message)):
	chunck = message[i:i+15]
	if(isPhoneNumber(chunck)):
		print("Найден номер телефона : " + chunck)
		nCountNumbers += 1
print("Найдено ", nCountNumbers, " номеров")
print("Готово")