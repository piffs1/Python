#! python3
# pw.py - Программа для незащищенного хранения паролей.

PASSWORDS = {"email" : "213456",
			"blog" : "214245",
			"vlog" : "52152"}

import sys , pyperclip
if len(sys.argv) < 2:
	print("Использование python pw.py [имя учетной записи] - "
		"копирование пароля учетной записи")
	sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print("Пароль для " + account + " скопирован в буфер")
else:
	print("Что-то пошло не так")