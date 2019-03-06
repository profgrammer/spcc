from tables import mdt, mnt, ala
import re
import time
f = open('intermediate.txt', 'r')

lines = f.readlines()

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
            if first[0].startswith('&'):
                _ala.append(first[0])
            else:
                _ala.append(None)
            for k in range(1, len(first)):
                _ala.append(first[k])
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
                        l = l.replace(a[k], _ala[ind])
                    print(l)
                mdtp += 1
            break
        else:
            print(lines[i].replace('\n', ''))
            break

    i += 1

t2 = time.time()

print('time for pass 2: ' + str(t2 - t1))
