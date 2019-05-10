def lstToStr(a_list):
	result = ""
	for i in range(len(a_list)-1):
		result += a_list[i] +", "
	result += "and " + a_list[len(a_list)-1]
	return result
spam = ["apples", "bananas", "tofu", "cats"]

print(lstToStr(spam))