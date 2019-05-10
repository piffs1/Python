import re

vowelRegex = re.compile(r'[a-zA-Z0-9]') # Поиск всех английских букв в нижнем и верхнем реестре
vowelRegex2 = re.compile(r'[^a-z .A-Z0-9]')
print("".join(vowelRegex.findall("Robocop eats детскую food. BABY FOOD.")))
print("".join(vowelRegex2.findall("Robocop eats детскую food. BABY FOOD.")))

beginsWithHello = re.compile(r'^\w+ello') # должно начинаться с Hello

print(beginsWithHello.search("Hello World!"))
print(beginsWithHello.search("hello World!"))
print(beginsWithHello.search("World hello!"))

endsWithNumber = re.compile(r'\d+$') # заканчиваться на цифру

print(endsWithNumber.search("Your number is 12"))

strOnlyNumber = re.compile(r'^\d+$')

print(strOnlyNumber.search("1234567890"))
print(strOnlyNumber.search("12345x67890"))



