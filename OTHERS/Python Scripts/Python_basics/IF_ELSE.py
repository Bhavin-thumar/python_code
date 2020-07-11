num = 3
if num > 0:
    print(num,'is a positive number')
print("this is always printed")

num = -1
if num > 0:
    print(num, 'is positive number')
print('this is also always printed')

num = float(input("enter the number :"))
if num > 0:
    print('positive number')
elif num == 0:
    print('zero')
else:
    print('negative number')