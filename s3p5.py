a=[]
n=int(input("enter no of terms"))
for i in range (0,n):
  b=int(input("enter the number"))
  a.append(b)
  a.sort()
print(a[(n-1)//2])
