i = 0

while (i < 10):
	if(i==3):
		i+=1
		continue
	print ("i step :", i)
	i+=1
	if i == 5:
		print ("i=5, breaking..")
		break