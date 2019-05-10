import re

spam = '''Serve the public Trust
Protect the innocent.
Uphold the law'''

noNewLineRegex = re.compile(".*")
print(noNewLineRegex.search(spam))

NewLineRegex = re.compile(".*",re.DOTALL)
print(NewLineRegex.search(spam).group()) # OK

#ignore register	
robocop = re.compile(r'robocop', re.I) # re.I == re.IGNORECASE
print(robocop.search("RoBoCop is part man, part machine, all cop"))
print(robocop.findall("RoBoCop is part man robocop"))