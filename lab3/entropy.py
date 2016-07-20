import sys, math

data = input()

def entropy(data):
	P = [ float(data.count(c)) / len(data) for c in dict.fromkeys(list(data)) ]
	H = - sum([ p * math.log(p) / math.log(2.0) for p in P ])
	return H

print (entropy(data))
