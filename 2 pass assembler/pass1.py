import re
from motpot import mot, pot 

f = open('samplePass1.txt', 'r')
tables = open('tables.py', 'w')
intermediate = open('intermediate.txt', 'w')
symbols = []
literals = []

lc = 0
ex = False
count = 1
for line in f.readlines():
	if ex: 
		break
	toWrite = True
	words = re.split(r'[,\s]+', line)
	words.pop()
	# print(words)
	lineans = ""
	# print(lc)
	for i in range(len(words)):
		word = words[i].lower()
		if word == '' or word == ' ':
			continue
		if i == 0:
			if word in pot:
				if word == 'using' or word == 'drop':
					break
				if word == 'start':
					lc = int(words[i+1])
					break
				if word == 'ltorg' or word == 'end':
					found = False
					for literal in literals:
						if literal["value"] == None:
							found = True
							break
					if found:
						lc += 8 - (lc % 8)
						for literal in literals:
							if literal['value'] == None:
								literal["value"] = lc
								literal['count'] = count
								lc += literal["length"]
					if word == 'end':
						ex = True

			elif word in mot.keys():
				lc += mot[word]["length"]
			else:
				if word not in symbols:
					if words[i+1].lower() == 'equ':
						val = lc if words[i+2] == '*' else int(words[i+2])
						ar = 'r' if words[i+2] == '*' else 'a'
						symbols.append({"symbol": word, "value": val, "length": 1, "ar": ar})
						toWrite = False
						break
					elif words[i+1].lower() == 'ds':
						temp = int(words[i+2][:-1])
						symbols.append({"symbol": word, "value": lc, "length": 4, "ar": "r"})
						lc += 4 * temp
					elif words[i+1].lower() == 'dc':
						symbols.append({"symbol": word, "value": lc, "length": 4, "ar": "r"})
						for j in range(i+2, len(words)):
							arr = re.split(r'([^0-9])', words[j])
							for x in arr:
								if x.isnumeric():
									lc += 4
					else:
						symbols.append({"symbol": word, "value": lc, "length": 1, "ar": "r"})
						

		else:
			if word in pot:
				if word == 'using' or word == 'drop':
					break
				if word == 'start':
					lc = int(words[i+1])
					break
			elif word in mot.keys():
				lc += mot[word]["length"]
			else:
				if word.startswith('='):
					if word not in literals:
						literals.append({"literal": word, "value": None, "length": 4, "ar": "r", "count": None})
	# print(lc)
	if toWrite:
		intermediate.write(line)
		count += 1

print(lc)
tables.write("symbols = " + str(symbols))
tables.write("\n\nliterals = " + str(literals))


