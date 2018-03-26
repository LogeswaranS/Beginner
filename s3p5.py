z=[]
n=int(input("enter no of terms"))
for i in range (0,n):
  b=int(input("enter the number"))
  z.append(b)
  z.sort()
print(z[(n-1)//2])
