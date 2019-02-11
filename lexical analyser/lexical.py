import re

keywords = ['int', 'float', 'double', 'long', 'void']
operators = ['+', '-', '*', '/', '%']
ssymbols = ['{', '}', ';', '\"', '\'', '(', ')', '=']
predef = ['main', 'printf']
symbols = list()
literals = list()


f = open("sample.txt", "r")
out = open("out1.txt", "w")


count = 1
for line in f.readlines():
	
	words = re.split('({|}|(|)|+|-|/|*|%|;|\'|\")', line)
	# print(words)
	lineans = ""
	for word in words:
		if word == '' or word == ' ' or word == '\n':
			continue
		if word in keywords:
			lineans += "<keyword#" + str(keywords.index(word)) + "> "
		elif word in operators:
			 lineans += "<operator#" + str(operators.index(word)) + "> "
		elif word in ssymbols:
			lineans += "<special#" + str(ssymbols.index(word)) + "> "
		elif word in predef:
			lineans += "<predef#" + str(predef.index(word)) + "> "
		else:
			if word[0].isalpha() or word[0] == '_':
				if word not in symbols:
					symbols.append(word)
				lineans +=  "<symbol#" + str(symbols.index(word)) + "> "
			elif word[0].isnumeric():
				if word not in literals:
					literals.append(word)
				lineans +=  "<symbol#" + str(literals.index(word)) + "> "
	if lineans != "":
		out.write(lineans + "\n")

print(symbols)
print(literals)

