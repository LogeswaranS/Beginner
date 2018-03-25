def main():
   
 num = int(input(""))
 sum = 0
 temp = num
 while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
 if num == sum:
   print("Yes its an armstrong number")
 else:
   print("No its not an armstrong number")

if __name__ == '__main__':
    main()
