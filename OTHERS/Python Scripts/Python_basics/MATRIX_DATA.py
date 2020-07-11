# Matrix Data : Data that is represented in tabular form.


a = [['Roy', 80, 75, 85, 90, 95],
     ['John', 75, 80, 75, 85, 100],
     ['Dave', 80, 80, 80, 90, 95]]

n = 3
m = 4
b = [0] * n
print(b)

for i in range(n):
    print(type(b[i]))               # output : class 'int'
    b[i] = [0] * m
    print(type(b[i]))               # output : class 'list'
print(b)                    # output : [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# create matrix using numpy

from numpy import *

x = range(16)

x = reshape(x, (4, 4))
print(x)