spam = "HEllO мИР!"
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)
print(spam.isupper())
print(spam.islower())
print("spam isalpha ","spam".isalpha())
print("sp12 isalnum", "sp12".isalnum()) # characters + numbers
print("sp12! isalnum", "sp12!".isalnum())
print("21345".isdecimal())
print("   ".isspace())
bacon = "Привет друг!"
print(bacon.istitle())
print(bacon[:6].istitle())