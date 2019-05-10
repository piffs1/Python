import pyperclip 			#buffer
pyperclip.copy("")
if(pyperclip.paste() == ""):
	print("Buffer is empty")