def eggs(someParameter):
	someParameter.append("Hello")
	return someParameter
spam = [1,2,3]
spam = eggs(spam)
print(spam) # [1,2,3,"Hello"]
