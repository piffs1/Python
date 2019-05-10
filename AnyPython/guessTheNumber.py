import math , random
lowerBound = int(input("Введите нижнюю границу "))
upperBound = int(input("Введите верхнюю границу "))
attempts = int(math.log2(upperBound-lowerBound) +1)
print ("Задумано число от ",lowerBound , "до" , upperBound, "Попробуй угадай его. Тебе понадобится ", attempts, " попыток")
number = random.randint(lowerBound,upperBound)
for i in range(attempts):
	print (i+1, " попытка. Ваш вариант : ", end="")
	guess = int(input())
	if(guess == number):
		print("Yaaay! Its ", guess)
		break
	if(guess > number):
		print("Это число меньше задуманного")
	else:
		print("Это число больше задуманного")