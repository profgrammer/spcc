import re
from tables import literals, symbols
from motpot import mot, pot

f = open('intermediate.txt', 'r')
base = [-1 for i in range(16)]
lc = 0
count = 1

def find_nearest(ea):
	min_dist = 100000
	reg = -1
	for i in range(len(base)):
		if base[i] != -1 and abs(ea - base[i]) < min_dist:
			min_dist = abs(ea - base[i])
			reg = i
	return reg



for line in f.readlines():

	words = re.split(r'[,\s]+', line)
	words.pop()
	for i in range(len(words)):
		word = words[i].lower()
		if word == '' or word == ' ':
			continue
		
		if word in pot:
			if word == 'start':
				lc = int(words[i+1])
				# print(lc)
				break
			elif word == 'using':
				arg1, arg2 = 0, 0
				if words[i+1] == '*':
					arg1 = lc
				else:
					for symbol in symbols:
						if symbol["symbol"] == words[i+1].lower():
							arg1 = symbol["value"]			
				if words[i+2].isnumeric():
					arg2 = int(words[i+2])
				else:
					for symbol in symbols:
						if symbol["symbol"] == words[i+2].lower():
							arg2 = symbol["value"]
				base[arg2] = arg1
			elif word == 'ltorg' or word == 'end':
				# print(count)
				found = False
				for literal in literals:
					if literal['count'] == count:
						found = True
				if found:
					lc += 8 - (lc % 8)
					for literal in literals:
						if literal['count'] == count:
							print(literal['value'], literal['literal'])
							lc += literal['length']
			elif word == 'ds':
				val = int(words[i+1][:-1])
				
				print(lc, word, '------------')
				lc += 4 * val
			elif word == 'dc':
				for j in range(i+1, len(words)):
					arr = re.split(r'([^0-9])', words[j])
					for x in arr:
						if x.isnumeric():
							print(lc, x)
							lc += 4

		elif word in mot:
			
			if mot[word]["type"] == 'rr':
				arg1, arg2 = -1, -1
				if word == 'br':
					command = 'bcr'
					arg1 = 15
					arg2 = 0
					if words[i+1].isnumeric():
						arg2 = int(words[i+1])
					print(str(lc) + " " + str(command) + " " + str(arg1) + ", " + str(arg2))
					continue
				if words[i+1].isnumeric():
					arg1 = int(words[i+1])
				elif words[i+1].startswith('='):
					for literal in literals:
						if literal['literal'] == words[i+1].lower():
							arg1 = literal['value']
				else:
					for symbol in symbols:
						if symbol['symbol'] == words[i+1].lower():
							arg1 = symbol['value']
				if words[i+2].isnumeric():
					arg1 = int(words[i+2])
				if words[i+2].startswith('='):
					for literal in literals:
						if literal['literal'] == words[i+2].lower():
							arg2 = literal['value']
				else:
					for symbol in symbols:
						if symbol['symbol'] == words[i+2].lower():
							arg2 = symbol['value']
				print(lc, word, arg1, ", ", arg2)

			elif mot[word]["type"] == 'rx':

				arg1 = 0
				
				if word == 'bne':
					arg1 = 7
					ea = 0
					if words[i+1].startswith('='):
						for literal in literals:
							if literal['literal'] == words[i+1].lower():
								ea = literal['value']
					else:
						for symbol in symbols:
							if symbol['symbol'] == words[i+1].lower():
								ea = symbol['value']

					reg = find_nearest(ea)
					cbr = base[reg]
					d = ea - cbr
					index = 0
					print(str(lc) + " " + 'bc' + " " + str(arg1) + ", " + str(d) + "(" + str(index) + ", " + str(reg) + ")")
				else:
					if words[i+1].isnumeric():
						arg1 = words[i+1].lower()
					elif words[i+1].startswith('='):
						for literal in literals:
							if literal['literal'] == words[i+1].lower():
								arg1 = literal['value']
					else:
						for symbol in symbols:
							if symbol['symbol'] == words[i+1].lower():
								arg1 = symbol['value']

					ea = 0
					args = re.split(r'[\(\)]+', words[i+2])
					args.pop()
					# print(args)
					index = 0
					if words[i+2].startswith('='):
						for literal in literals:
							if literal['literal'] == words[i+2].lower():
								ea = literal['value']
					elif len(args) == 2:
						for symbol in symbols:
							if symbol['symbol'] == args[0].lower():
								ea = symbol['value']
						if args[1].isnumeric():
							index = int(args[1])
						else:
							for symbol in symbols:
								if symbol['symbol'] == args[1].lower():
									index = symbol['value']
					else:
						for symbol in symbols:
							if symbol["symbol"] == words[i+2].lower():
								ea = symbol["value"]
					reg = find_nearest(ea)
					cbr = base[reg]
					d = ea - cbr
					print(str(lc) + " " + word + " " + str(arg1) + ", " + str(d) + "(" + str(index) + ", " + str(reg) + ")")
			lc += mot[word]['length']
	count += 1	
				
							
		




















	
