def spam():
#	global eggs # создается глобальная переменная, локальной переменной не создается
	eggs = "spam"

def spam2():
	global eggs # обращение к глобальной переменной 
	eggs = "spam"

def bam(name):
	print (eggs + str(name))

eggs = "global"

print (eggs)
spam()
spam2()
bam(12)