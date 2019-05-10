import os


print(os.path.abspath("."))
print(os.path.abspath("..\\Scripts"))


print(os.path.relpath("C:\\Windows", "C:\\")) # windows
print(os.path.relpath("C:\\Windows", "C:\\spam\\eggs")) # ..\..\Windows
# .\ Текущий каталог ..\ Предыдущий каталог

path = "C:\\Windows\\System32\\calc.exe"

print(os.path.basename(path)) # calc.exe
print(os.path.dirname(path)) # C:\\Windows\\System32

print(os.path.split(path)) # ('C:\\Windows\\System32', 'calc.exe') Tuple
print((os.path.dirname(path), os.path.basename(path))) # Equal ^

print(path.split(os.path.sep)) #['C:', 'Windows', 'System32', 'calc.exe']

print(os.path.getsize(path)) # 27648 -> байт весит calc.exe
print(os.listdir("C:\\")) # Показывает все директории и файлы

print("==========================================")


# Считает только сами файлы. Размер папок не учитывается