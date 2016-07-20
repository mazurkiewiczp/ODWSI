import crypt, sys

alfabet = 'abcdefghijklmnopqrstuvwxyz'
data = open(sys.argv[1])

for line in data:
	crypted = line.split(":")[1].strip()
	for a in alfabet:
		for b in alfabet:
			for c in alfabet:
				guess = crypt.crypt(a+b+c,crypted)
				if guess == crypted:
					print(line.split(':')[0] + ': ' + a+b+c)
