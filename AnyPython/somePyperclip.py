import pyperclip

text = pyperclip.paste()

# TODO: разделить строки и добавить звездочки

lines = text.split("\n")
for i in range(len(lines)):
	lines[i] = lines[i].lstrip()
print(lines)
text = "\n".join(lines)
pyperclip.copy(text)
