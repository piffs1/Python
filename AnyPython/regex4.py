import re

#. это один символ .at = cat, fat, lat, mat smth
# чтобы искать точку, необходимо добавить \.

atRegex = re.compile(r'.at')

print(atRegex.findall("The cat in the hat sat on the flat mat."))

nameRegex = re.compile(r'First name: (.*) Last Name: (.*)')

print(nameRegex.search('First name: Al Last Name: Sweigart').group(1))
print(nameRegex.search('First name: Al Last Name: Sweigart').group(2))

nonJadniySearch = re.compile(r'<.*?>') # Если r'<.*>' -> будет как можно больше текста вырвать
print(nonJadniySearch.search("<To serve man> for dinner.>"))

