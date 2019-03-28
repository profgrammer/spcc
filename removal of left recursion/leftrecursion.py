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


# if S -> Xa and X -> Sb then replace X in S ie S -> Sba
def step1(lines):
    ans = list()
    for i in range(len(lines)):
        toReplace = False
        line = lines[i]
        s = line["left"]
        newLeft = s
        newRight = list()
        for r in line["right"]:
            x = r[0]
            if x.isupper() and x != s:
                for j in range(i+1, len(lines)):
                    X = lines[j]["left"]
                    if X == x:

                        found = False
                        for right in lines[j]["right"]:
                            if right[0] == s:
                                # print(s, x, X)
                                found = True
                                break
                        if found:
                            toReplace = True
                            for right in lines[i]["right"]:
                                if not right.startswith(X):
                                    newRight.append(right)
                            for right in lines[j]["right"]:
                                newRight.append(right + r[1:])
        if toReplace:
            ans.append({"left": newLeft, "right": newRight})
            # print(ans[-1])
        else:
            ans.append(lines[i])
    return ans

def removeLeftRecursion(line):
    cleaned = line
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


lines = list()
for line in f.readlines():
    cleaned = clean(line)
    lines.append(cleaned)
lines = step1(lines)
# print(lines)
print("Step 1: removing indirect left recursion")
printProductions(lines)
print("After removing left recursion:")
for line in lines:
    ans = removeLeftRecursion(line)
    # print(ans)
    printProductions(ans)
