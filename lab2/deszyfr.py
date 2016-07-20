import sys, re, string

stat = {}
msg = input()
for znak in msg:
	if znak in stat:
		stat[znak] += 1
	else:
		stat[znak] = 1

naj = 0
litera = 'a'
for znak in stat:
	if stat[znak] > naj:
		litera = znak
		naj = stat[litera]

alfabet = 'abcdefghijklmnopqrstuvwxyz'
ile = 0
for i in range(26):
	if litera == alfabet[i]:
		ile = i
ile = -ile
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
print(-ile)
