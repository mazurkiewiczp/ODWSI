import sys

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

keystream = genStream(iniReg(sys.argv[1]), sys.argv[2])
msg = ''
for c in sys.argv[2]:
	msg+=str(chr(int(format(ord(c) ^ next(keystream),'02X'),16)))
print(msg)
