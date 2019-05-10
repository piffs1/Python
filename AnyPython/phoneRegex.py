import re, pyperclip

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?
	(\s|-|\.)
	\d{3}
	(\s|-|\.)
	\d{4}
	(\s*(ext|x|ext.)\s*\d{2,5})?
	)''', re.VERBOSE)
# re.VERBOSE -> Для явного указания, что удобнее работать в многострочном режиме

text = pyperclip.paste()


phoneRegX = re.compile(r'''
	
	(^\+?\d|\d)		# plus7 или 8
	\W*				# скобка
	(\d\d\d)		# region
	\W*				# скобка
	(\d\d\d)
	\W* 
	(\d\d)
	\W*
	(\d\d)
	(\d*)
# TODO: 
# 8-916-917-8-918-919-88-88 -> 8-918-919-88-88 WRONG
# 8912422591232 -> 89124225912 WRONG
	''', re.VERBOSE)

phones = phoneRegX.findall(text)

print("Найдены номера : ")

for phones in phoneRegX.findall(text):
	if(phones[len(phones)-1]==""):
		print(phones[0],end="(")
		print(phones[1],end=")")
		print(phones[2],end="-")
		print(phones[3],end="-")
		print(phones[4])


#phoneRegX = re.compile(r'''
#	(^\+\d|\d)		# plus7 или 8
#	\W*  			# скобка
#	(\d\d\d)+		# region
#	\W*				# скобка
#	(\d\d\d)+
#	\W*
#	(\d\d)+
#	\W*
#	(\d\d)+
#	
#	''', re.VERBOSE)
#matches=[]


# 8-916-111-11-11	#OK
# 8495-111-11-11
# 888888888888		#NOT OK
# 8912422591232		#NOT OK
# 89122246587
# 891755766111 
# 8-917-557-66-11
# 8-916-917--918-919-88-88
# 7 (916) 258-6586

#phoneRegHelp = re.compile(r"(^\+?\d|\d)\W*")
# +
# 7(495)369-08-00 	#OK
# +7(917)222-22-22 	#OK
# 8(917)668-11-21	#OK
# 8-916-111-11-11	#OK
# 8495-111-11-11
# 888888888888		#NOT OK
# 8912422591232		#NOT OK
# 89122246587
# 891755766111 
# 8-917-557-66-11
# 8-916-917-8-918-919-88-88
# +7 (916) 258-6586