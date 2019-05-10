import os

myFiles = ["accounts.txt", "details.csv", "invite.docx"]
for filename in myFiles:
	print(os.path.join("C:\\Users\\as", filename)) # C:\Users\as\filename

print(os.getcwd()) # current directory
os.chdir("C:\\Windows")
print(os.getcwd()) # C:\Windows
#os.chdir("C:\\w")  # ERROR
# os.makedirs -> Создание каталогов
