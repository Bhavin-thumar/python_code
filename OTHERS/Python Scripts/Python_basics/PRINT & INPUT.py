# print(...)
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

# if you want to print raw data add r before quotes
# print(r'raw data')

# input(prompt=None, /)
#     Read a string from standard input.  The trailing newline is stripped.\

a, b = 1, 2
print(f'the value of a : {a} and value of b : {b}')

print(1, 2, 3, 4, 5, sep='%')

num = float(input("enter the number :"))
if num > 0:
    print('positive number')
elif num == 0:
    print('zero')
else:
    print('negative number')