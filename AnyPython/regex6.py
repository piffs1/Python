result = re.match(r"AV", "AV Analytics Vidhya AV")

print( result.start() ) # match -> производит поиск вначале строки
print( result.end() ) # start-end -> позиции в строке