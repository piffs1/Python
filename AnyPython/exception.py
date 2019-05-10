def divide(divideBy):
	return 42 / divideBy

try:
	print(divide(12))
	print(divide(0))
	print(divide(1))
except ZeroDivisionError:
	print("Error. DELISH NA NOL")