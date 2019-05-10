import sys

while True:
	response = input ("Напиши слово ")
	if (response == "слово"):
		sys.exit() # sys.exit() equal exit() 
	print ("Ты написал " + response + ".")