from tables import mdt, mnt, ala
import re
import time
f = open('intermediate.txt', 'r')

lines = f.readlines()

def findIndex(macroName, word):
	values = list()
	for i in range(len(ala[macroName])):
		values.append(ala[macroName][i]["value"])
	return values.index(word)

def findParameter(_ala, ind):
    for param in _ala:
        if param["index"] == ind:
            return param["value"]

i = 0

t1 = time.time()
while i < len(lines):
    lines[i] = lines[i].lower()
    words = re.split(r'[\s,]+', lines[i])
    words.pop()
    for j in range(len(words)):
        word = words[j].lower()

        if word in mnt.keys():
            mdtp = mnt[word]["index"]
            first = re.split(r'[\s,]+', lines[i])
            first.pop()
            _ala = list()
            # print("first=", first)
            if ala[word][0]["value"] is not None:
                _ala.append({"index": 0, "value": first[0]})
                for k in range(2, len(first)):
                    # keyword or default parameter
                    if first[k].startswith("&"):
                        x = re.split("=", first[k])
                        # keyword
                        if len(x) == 2:
                            ind = findIndex(word, x[0])
                            _ala.append({"index": ind, "value": x[1]})
                        # default
                        else:
                            ind = findIndex(word, x[0])
                            _ala.append({"index": ind, "value": ala[word][ind]["default"]})
                    else:
                        # ind = findIndex(word, first[k])
                        _ala.append({"index": len(_ala), "value": first[k]})

            else:
                _ala.append({"index": 0, "value": None})
                for k in range(1, len(first)):
                    # keyword parameter
                    if first[k].startswith("&"):
                        x = re.split("=", first[k])
                        # keyword
                        if len(x) == 2:
                            ind = findIndex(word, x[0])
                            _ala.append({"index": ind, "value": x[1]})
                        else:
                            ind = findIndex(word, x[0])
                            _ala.append({"index": ind, "value": ala[word][ind]["default"]})
                    else:
                        # ind = findIndex(word, first[k])
                        _ala.append({"index": len(_ala), "value": first[k]})
            # filling in default values
            for it in range(len(ala[word])):
                obj = ala[word][it]
                if obj["type"] == "d":
                    found = False
                    for obj1 in _ala:
                        if obj1["index"] == i:
                            found = True
                            break
                    if not found:
                        ind = findIndex(word, obj["value"])
                        _ala.append({"index": ind, "value": ala[word][ind]["default"]})
            # print(_ala)
            mdtp += 1
            mend = False
            while not mend:
                l = mdt[mdtp]
                if l == 'mend':
                    mend = True
                else:
                    pattern = '(#[0-9]+)'
                    a = re.findall(pattern, l)
                    for k in range(len(a)):
                        ind = int(a[k].replace('#', ''))
                        val = findParameter(_ala, ind)
                        l = l.replace(a[k], val)
                    print(l)
                mdtp += 1
            break
        else:
            if j == len(words) - 1:
                print(lines[i].replace('\n', ''))
                break


    i += 1

t2 = time.time()

print('time for pass 2: ' + str(t2 - t1))
