spam = [ 0, 1, 2, 3, 4, 5 ]
cheese = spam # Если это список, то присваивется ссылка cheese = &spam 
print(spam) # REFID(NUMBER) -> область памяти аналогично с &
print(cheese)
cheese[1] = "Hello!"
print(spam)
print(cheese) 
# ВАЖНАЯ РЕМАРКА! В НЕИЗМЕНЯЕМЫХ ТИПАХ ХРАНЯТСЯ ДАННЫЕ(СТРОКИ, КОРТЕЖИ)
# В ИЗМЕНЯЕМЫХ ДАННЫХ ХРАНИТСЯ ССЫЛКА НА ОБЪЕКТ (LIST)