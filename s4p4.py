fname = input("Enter name of the file: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("No. of lines")
print(num_lines)
