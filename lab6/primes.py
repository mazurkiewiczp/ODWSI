import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

def NWD(a,b):
	r=a%b
	a=b
	b=r
	if (b==0): 
		return a
	else:
		return NWD(a,b)

def areCoprimes(a,b):
	if NWD(a,b)==1:
		print(str(a) + " i " + str(b) + " sa wzglednie pierwsze")
	else:
		print(str(a) + " i " + str(b) + " nie sa wzglednie pierwsze")

areCoprimes(a,b)
