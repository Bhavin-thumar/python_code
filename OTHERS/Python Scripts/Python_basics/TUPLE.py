# Tuple are similar to list only difference it is immutable i.e cannot be change/add/delete its element .
# Tuple that contain immutable elements can be used as key for a dictionary.
# Tuple are write protected.
# Tuple for hetrogeneous data type and List for homogeneous data type.

# Creating Tuple

my_tuple = ()
my_tuple_2 = ("mouse", [8, 4, 6], (1, 2, 3))

# Accessing elements of Tuple
# 1. Indexing
# 2. Negative Indexing
# 3. Slicing

print(my_tuple_2[0])                    # output : mouse
print(my_tuple_2[2][2])                 # output : 3
print(my_tuple_2[-1])                   # output : (1, 2, 3)
print(my_tuple_2[0:2])                  # output : ('mouse', [8, 4, 6])

# Adding(+) and Multiply(*)

print((1, 2, 3) + (4, 5, 6))            # output : (1, 2, 3, 4, 5, 6)
print(("hi",) * 3)                      # output : ("hi", "hi", "hi")

# Deleting a Tuple

# del tuple_name

my_tuple_3 = ('a', 'p', 'p', 'l', 'e')
print(my_tuple_3.count('p'))            # output : 2
print(my_tuple_3.index('l'))            # output : 3
print('a' in my_tuple_3)                # output : True
print('g' not in my_tuple_3)            # output : True