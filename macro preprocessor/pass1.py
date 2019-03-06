import re
import time

f = open('sample.txt', 'r')
out = open('intermediate.txt', 'w')
tables = open('tables.py', 'w')

mnt = {}
mdt = []
ala = {}

macroStart = False
index = 0

lines = f.readlines()
macroName = None

i = 0
t1 = time.time()
while i < (len(lines)):
	lines[i] = lines[i].lower()
	words = re.split(r'[\s,]+', lines[i])
	words.pop()
	# print(words)
	mdtLine = ''
	macroLine = False
	for j in range(len(words)):
		word = words[j].lower()

		if macroStart:
			macroLine = True
			if word == 'mend':
				macroStart = False
				mdtLine += word
				macroName = None
			elif word.startswith('&'):
				# print(str(ala[macroName]))
				mdtLine += (", #" + str(ala[macroName].index(word)) + " ")
			else:
				mdtLine += (word + " ")

		if word == 'macro':
			macroLine = True
			macroStart = True
			# processing macro name
			twords = re.split(r'[\s,]+', lines[i+1])
			lines[i+1] = lines[i+1].lower()
			# mdt.append(lines[i+1])
			mdtLine = lines[i+1].replace('\n', '')
			i += 1
			twords = [x.lower() for x in twords]
			if twords[0].startswith('&'):
				macroName = twords[1].lower()
				ala[macroName] = list()
				ala[macroName].append(twords[0].lower())
			else:
				macroName = twords[0].lower()
				ala[macroName] = list()
				ala[macroName].append(None)
			# mnt.append({"name": macroName, "mdtindex": len(mdt)})
			mnt[macroName] = {"index": len(mdt)}
			for k in range(1, len(twords)):
				if twords[k].startswith('&'):
					ala[macroName].append(twords[k])
			break
	if mdtLine != '':
		mdt.append(mdtLine)
	if not macroLine:
		out.write(lines[i].lower())
		print(lines[i].lower().replace('\n', ''))
	i += 1
t2 = time.time()
print("mdt = " + str(mdt))
print("mnt = " + str(mnt))
print("ala = " + str(ala))
tables.write("mdt = " + str(mdt) + "\n")
tables.write("mnt = " + str(mnt) + "\n")
tables.write("ala = " + str(ala) + "\n")
# print(str(t1) + " " + str(t2))
print("Execution time = " + str(t2 - t1))
