x=input("\nenter the name to check palindrome or not:")
y=list(reversed(x))
d=list(reversed(y))
if y==d:
    print("\nyes")
else:
    print("\nno")
