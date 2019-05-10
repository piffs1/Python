import pprint
message = "It was a bright cold day in April, and the clocks were striking thirtheen"
count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] += 1
for lst in count.items():
	print(lst[0] + " -> " + str(lst[1]))
pprint.pprint(count)