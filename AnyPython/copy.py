import copy
spam = list("ABCD")
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)
# ОТЛИЧИЕ COPY ОТ DEEPCOPY
# ЕСЛИ СПИСОК СОДЕРЖИТ ВНУТРИ СЕБЯ ЕЩЕ ЛИСТЫ
# ТО НЕОБХОДИМО ВЫЗВАТЬ DEEPCOPY
# ЕСЛИ ПРОСТО ЛИСТ, ТО COPY, ПОТОМУ ЧТО ЕСЛИ ВЫЗВАТЬ
# COPY ДЛЯ ВЛОЖЕННОГО ЛИСТА, ТО ОН СКОПИРУЕТ ССЫЛКУ
# Насчет изменяющихся и неизменяющихся типов. 
# если можно удалить или добавить в структуру данных -> это изменяющиеся
