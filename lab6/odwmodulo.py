import sys

u = 1
w = int(sys.argv[1])
x = 0
z = int(sys.argv[2])

while (w!=0):
	if (w<z):
		u,x = x,u
		w,z = z,w
	q=int(w/z)
	u=u-q*x
	w=w-q*z

if(z==1):
	if(x<0):
		x=x+int(sys.argv[2])
	print(str(x))
else:
	print("BRAK")
