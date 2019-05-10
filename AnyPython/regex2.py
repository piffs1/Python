import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall("Сотовый : 415-555-9999, мобильный 212-555-0000")
print(mo)

#re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') -> вывод кортежей
# ПОИСК ПО \d -> Любая цифра от 0 до 9
# ПОИСК ПО \D -> Любой символ, не являющийся цифрой
# Поиск \w Любая буква, цифра или символ подчеркивания(словарные символы)
# \W любой символ, не являющийся \w
# \s Символ пробела, табуляции или новой строки ' '. '\t', '\n'
# \S наборот

xmasReges = re.compile(r'\d+\s\w+') # цифр n-ое количество, пробел, символов n-ое количество
print(xmasReges.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings"))

