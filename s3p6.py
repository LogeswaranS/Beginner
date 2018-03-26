x=[]
y=int(input("Enter Number of Elements:"))
for i in range(1,y+1):
    z=int(input(" "))
    x.append(z)
#x.sort()
print("Median Element is:",x[int((y-1)/2)])
