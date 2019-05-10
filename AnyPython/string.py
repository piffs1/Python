print ("Hello world!")
print ("What's your name ?")
name = input()
print ("Nice to meet you", name)
print ("Length of your name is ", len(name))
age = input("What's your age ? ") #age request
print ("You will be", int(age)+1, "in a year")
print ("After two years you will be " + str(int(age)+2) + "!")
for i in name:
	print("* * *" + i + "* * *")
for i in age:
	print("* * *" + i + "* * *")
