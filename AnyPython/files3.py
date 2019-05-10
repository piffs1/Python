import os

nTotalSize = 0
path = "C:\\AMD"
for filename in os.listdir(path):
	print(os.path.join(path, filename), end= "\t")
	print(os.path.getsize(os.path.join(path, filename)), end = "\n")
	nTotalSize = nTotalSize + os.path.getsize(os.path.join(path, filename))
print("Bytes =" ,nTotalSize)
print("KB = ", nTotalSize / 1024)
print("MB = ", nTotalSize / 1024 / 1024)
# Считает некорректно папки
# sum([os.path.getsize(f) for f in os.listdir('.') if os.path.isfile(f)])