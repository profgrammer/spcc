# S-> aA
# A-> bA|c

ind = 0
temp = 0

def S(ind):
	t = ind
	if s[ind] == 'a':
		ind += 1
		x = A(ind)
		if x["val"]:
			if x["ind"] == len(s):
				#print(x["ind"], len(s))
				return True
	return False

def A(ind):
	if ind >= len(s):
		return {"val": False, "ind": ind}
	t = ind
	if s[ind] == 'b':
		ind += 1
		x = A(ind)
		if x["val"]:
			ind = x["ind"]
			return {"val": True, "ind": ind}
	else:
		ind = t
		if s[ind] == 'c':
			ind += 1
			return {"val": True, "ind": ind}
	return {"val": False, "ind": ind}

s = input()
print(S(0))
