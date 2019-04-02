from precedence_table import t
import re

def pre(left, right):
    if left == 'x':
        return 1
    if right == 'x':
        return -1
    precedence = {"$": -1, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": 4}
    if precedence[left] == precedence[right]:
        return 2
    if precedence[left] > precedence[right]:
        return 1
    if precedence[left] < precedence[right]:
        return -1

def clean(line):
    line = line.rstrip()
    x = re.split(r'[->]+', line)
    left = x[0]
    right = re.split(r'[|]+', x[1])

    # print(left, right)
    return {"left": left, "right": right}

exp = input()

exp = "$" + exp + "$"


grammar = "E->E+E|E*E|(E)|x"
terminals = ["x"]
operators = ["+", "*", "-", "/", "^", "(", ")"]

cleanedGrammar = clean(grammar)


print(exp)

exp1 = ""

for i in range(1, len(exp)):
	left = exp[i-1]
	right = exp[i]
	precedence = pre(left, right)
	if precedence == -1:
		exp1 += left + "<"
	elif precedence == 1:
		exp1 += left + ">"
	elif precedence == 2:
		exp1 += left + "="
exp1 += "$"

temp = exp

print(exp1)

stack = list()
stack.append("$")
i = 1

while(True):
	symbol = exp[i]
	if(stack[-1] == "$" and symbol == "$"):
		break
	else:
		a = stack[-1]
		b = symbol
		precedence = pre(a, b)
		if precedence == -1 or precedence == 2:
			stack.append(b)
			i += 1
		elif precedence == 1:
			latest = stack[-1]
			stack.pop()
			top = stack[-1]
			while(pre(latest, top) == -1):
				latest = stack[-1]
				stack.pop()
				top = stack[-1]
				print("in while latest=", latest)
			print("handle =", latest)
			index = temp.find(latest)
			if latest in terminals:
				print("Reducing using production", cleanedGrammar["left"], "->", latest)
				temp = temp.replace(latest, cleanedGrammar["left"], 1)
				print(temp)
			elif latest in operators:
				production = temp[index-1] + latest + temp[index+1]
				print("Reducing using production", cleanedGrammar["left"], "->", production)
				temp = temp.replace(production, cleanedGrammar["left"], 1)
				print(temp)
		else:
			print("error")
			break
