x=int(input("\n Enter the number:"))
y=list(str(x))
z=len(y)
d=0
while z>0:
    if(int(y[d])%2==0):
        d=d+1
    else:
        print("\n",y[d])
        d=d+1
    z=z-1
