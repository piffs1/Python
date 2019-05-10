def hello(): # void hello()
	print("I'm function hello()")
def hello1(name): # void hello(name)
	print ("Hello " + str(name))
def one_or_two(number): # string one_or_two(number)
	if(int(number) == 1):
		return "You selected one!"
	else:
		return "You selected two!"
hello()
hello1("Boris!")
print (one_or_two(2))
