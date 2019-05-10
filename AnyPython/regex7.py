import re

namesRegex = re.compile(r"Agent \w+",re.I)
sup = namesRegex.sub("Agent CENSORED", "agent Alice gave the secret docs to Agent bob.") # sub(Помнять НА, поменять ИЗ)

agentNamesRegex = re.compile(r'Agent (\w)\w*')
sup1 = agentNamesRegex.sub(r'\1*****', 'Agent Alice told Agent Carol and Agent Eve')
# \1 -> Вставить в первую группу, определяется это
# re.compile(r'(group1)-(group2)..etc')
# для \1text1 -> group1, для \2text2 -> group2 
# получается строка выходная будет
# text1-text2

print(sup)

print(sup1)

multiRegex = re.compile(r'some', re.I | re.VERSBOSE | re.DOTALL) #OK