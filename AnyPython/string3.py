print("PICNIC ITEMS".center(16,"-"))
ma = {"sandwitches" : 4, "apples" : 12, "cups" : 4, "coockies" : 8000}
for lst in ma.items():
	print(lst[0].ljust(len("sandwitches")+2,".") + " " + str(lst[1]).ljust(4))
spam = " HEllo WRld! "
print(spam.strip()) #Удаляет пробелы слева и справа
print(spam.rstrip())
print(spam.strip(" HEl"))
spam2 = "SpamSpamSpamBaconSpamEggsSpam1SpamSpam"
print(spam2.strip("Samp")) 	# находит первый входной символ( из набора strip(arg) )
							# если такого нет, то завершается
# кроче strip(){rstrip(); lstrip()}
# идет только до того момента, пока совпадают символы из набора, как только какой
# либо символ не совпал завершает работу пример работы:
# "spamspam1spam4spam".strip("asmp1") -> lstrip() дошел до символа 4 и завершился
# rstrip() дошел до символа 4 с конца и завершился. символа нет в наборе