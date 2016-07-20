import sys, re, string

stat = {}
for line in sys.stdin.readlines():
        line = re.sub(r'\s', '', line)
        for znak in line:
                if znak in stat:
                        stat[znak] += 1
                else:
                        stat[znak] = 1

for znak in stat:
        print (str(znak) + "<=>" + str(stat[znak]))
