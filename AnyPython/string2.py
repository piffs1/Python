print("Hello world!".startswith("Hello")) # true проверяет на вхождение слова в строку
print("Hello world!".endswith("world!"))
print("ABC".join(["My", "Name", "is", "Boris!"]))
#join(list) list only
spam = "My name is Boris!"
print(spam.split())
print(spam.split("s"))
print(spam.split("X"))
#split(arg = " ") -> разделяет строку на элементы списка,
#если ввести символ, которого нет в строке, выведется полная строка
print("Hello".rjust(20,"*"))
print("Hello".ljust(20,"-"))
print("Hello".center(20))
print("Hello".center(120,"-"))
