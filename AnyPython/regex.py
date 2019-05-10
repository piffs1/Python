import re

phoneNumberRegex = re.compile(r"\d-(\d\d\d)-(\d\d\d)-(\d\d-\d\d)")

mo = phoneNumberRegex.search("Мой номер 8-912-123-45-12")
print(mo.group()) # equal group(0)
# Каждая скобка 1 группа. Идут слева направо
print(mo.groups()) # все группы, кроме 0

PNR = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")

mo = PNR.search('''Мой номер :
	(916) 624-1212''')
print(mo.groups())