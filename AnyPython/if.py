name = input( "Введите ваше имя " )
if (name == 'Борис'):
	flag = True
	flag2 = False
	surname = input ( "Введите вашу фамилию " )
	if(surname == "Котенок"):
		flag2 = True
	if (flag and flag2):
		print ("Тебя зовут Борис Котенок")
	elif (flag and not flag2):
		print ("Тебя зовут Борис, но ты не Котенок")
	elif (not flag and flag2):
		print ("Ты не Борис, но Котенок")
	else:
		print ("Ты и не Борис и не Котенок вовсе")
# print (flag)
