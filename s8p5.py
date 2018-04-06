n=input("\n Enter the name:")
m=list(n)
b=len(m)
f=b/2
c=list(str(f))
d=int(c[0])
d=d+1
print(m.replace(m[d],"*"))
