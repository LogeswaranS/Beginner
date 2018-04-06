a=int(input("Enter a number "))
b=[]
c=0
while(a>0):
    print(a)
    b.insert(c,a)
    c=c+1
    a=a/2
print(list(reversed(b)))
