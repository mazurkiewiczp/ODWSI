ile = input()
ile = int(ile)%26
alfabet = 'abcdefghijklmnopqrstuvwxyz'
msg = input()

for c in msg:
	if c.lower() in alfabet:
		for i in range(26):
			if c.lower() == alfabet[i]:
				k = (i+ile)%26
				if c.isupper():
					print(alfabet[k].upper(),end='')
				else:
					print(alfabet[k],end='')
				break
	else:
		print(c,end='')
print()		
