# A -> Aa|b
# remove left recursion using the rule
# A -> bA'
# A' -> eps|aA'

import re

f = open('input.txt', 'r')


def clean(line):
    line = line.rstrip()
    x = re.split(r'[->]+', line)
    left = x[0]
    right = re.split(r'[|]+', x[1])

    # print(left, right)
    return {"left": left, "right": right}

def removeLeftRecursion(line):
    cleaned = clean(line)
    left, right = cleaned["left"], cleaned["right"]
    alphas = list()
    betas = list()
    ans = list()
    for prod in right:
        if prod[0] == left:
            alphas.append(prod[1:])
        else:
            betas.append(prod)
    if len(alphas) == 0:
        ans.append({"left": left, "right": right})
        return ans
    else:
        leftdash = left + "\'"
        ans.append({"left": left, "right": [beta + leftdash for beta in betas]})
        tempright = [alpha + leftdash for alpha in alphas]
        tempright.append("#")
        ans.append({"left": leftdash, "right": tempright})
        return ans

def printProductions(rules):
    for rule in rules:
        ans = rule["left"] + " -> "
        for production in rule["right"]:
            ans += production + "|"
        ans = ans[:-1]
        print(ans)

for line in f.readlines():
    ans = removeLeftRecursion(line)
    printProductions(ans)
