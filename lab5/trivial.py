import sys

def trivial_hash(path):
	dane = open(path)
	h = 0
	for line in dane:
		for znak in line:
			h += ord(znak)
	dane.close()
	return h % 999

print(sys.argv[1] + " trivial hash: " + str(trivial_hash(sys.argv[1])))
print(sys.argv[2] + " trivial hash: " + str(trivial_hash(sys.argv[2])))
print()
while(trivial_hash(sys.argv[1])!=trivial_hash(sys.argv[2])):
	mod = open(sys.argv[2],'a')
	mod.write(' ')
print(sys.argv[1] + " trivial hash: " + str(trivial_hash(sys.argv[1])))
print(sys.argv[2] + "(zmodyfikowany) trivial hash: " + str(trivial_hash(sys.argv[2])))
