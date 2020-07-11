import os

print(os.getcwd())

with open(r"C:\Users\hardip thummar\Documents\Python Scripts\test.txt", 'r') as f:
    print(f.readline(), end='')
    print(f.tell())
    print(f.readline(), end='')
    print(f.tell())
    print(f.readlines())

mylist = []
mylist.append('s')
print(mylist)
