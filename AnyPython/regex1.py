import re

batRegex = re.compile(r'Ho(mer|mik|mosapiens|ld)')

mo = batRegex.search("Boris  sHomer simpson")

print(mo.group())

batRegex = re.compile(r'Bat(wo)?man') # (wo)? не обязательная часть, т.е. Batman и может быть Batwoman
mo = batRegex.search("The adventure of Batman")

print(mo.group())

mo2 = batRegex.search("the adventure of Batwoman")

print(mo2.group())

print(batRegex.search("the adventure of Batwowoman")) # NONE

batRegex = re.compile(r'Bat(wo)*man') #(wo)* встречается n-ое кол-во раз

mo = batRegex.search("The adventure of Batwowowowowowowowoman")

print(mo.group())

batRegex = re.compile(r'Bat(wo)+man') #(wo)+ встречается один или n-ое количество раз
#, но обязательно должно быть Batwowowowoman, Batwoman->ok Batman->error

# Конструкция re.compile(r'Ha{3}') -> означает, что мы ищем HaHaHa
# re.compile(r'Ha{3,5}') -> От HaHaHa до HaHaHaHaHa
# re.compile(r'Ha{3,5}?') -> Не жадный поиск выведет сначала короткую строку
# re.compile(r'Ha{3,5}') -> Жадный поиск выведт (Ha){5}