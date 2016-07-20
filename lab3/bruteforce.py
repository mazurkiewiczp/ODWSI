import sys, math

def entropy(data):
        P = [ float(data.count(c)) / len(data) for c in dict.fromkeys(list(data)) ]
        H = - sum([ p * math.log(p) / math.log(2.0) for p in P ])
        return H

def iniReg(key):
	s = bytearray(256)
	for i in range(256):
		s[i]=i
	keylength = len(key)
	j = 0
	for i in range(256):
		j = (j + s[i] + ord(key[i%keylength]))%256
		s[i], s[j] = s[j], s[i]
	return s

def genStream(s, val):
	i = 0
	j = 0
	while True:
		i = (i+1)%256
		j = (j+s[i])%256
		s[i], s[j] = s[j], s[i]
		k = s[(s[i]+s[j])%256]
		yield k

data = input()
alfabet = 'abcdefghijklmnopqrstuvwxyz'
klucz = ''
ent = 10
best = ''
msg = ''
for i in range(26):
	klucz += alfabet[i]
	for j in range(26):
		klucz += alfabet[j]
		keystream = genStream(iniReg(klucz), data)
		for c in data:
			msg+=str(chr(int(format(ord(c) ^ next(keystream),'02X'),16)))
		if entropy(msg) < ent:
			best = msg
			ent = entropy(msg)
		klucz = klucz[:-1]
		msg = ''
	klucz = ''

print(best)
