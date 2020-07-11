# Set is unordered collection of items. That means Indexing have no meaning.
# Every element is unique(no duplicates) and must be immutable i.e( which cannot be changed).
# However set itself is mutable. We can add or remove items from it.
# It can have any number of items and they may be of different types. But a set cannot have mutable elements like
# list, set or dictionary as its elements.
# Empty {} will create dictionary not a set.
# Frozenset has characteristics of set, but its element cannot be changed once assigned.
# Sets being mutable are unhashable, so they cannot be used as dictionary keys. On other hand, frozensets are hashable
# so they can be used as dictionary keys.

my_set = {1, 2, 3, (3, 4), 5}
print(my_set)                                                   # Output : {1, 2, 3,(3, 4), 5}
# my_set2 = {1, 2, [3, 4]}
# print(my_set2)                                                # Output : TypeError: As set cannot have list as element

# add() : add single element to set
# update() : add multiple elements (must be enclosed with list,tuple or dictionary) to set

my_set.add(6)
print(my_set)                                           # output : {1, 2, 3, 4, 5, 6}
my_set.update([7, 8, 9])
print(my_set)                                           # output : {1, 2, 3, 4, 5, 6, 7, 8, 9}

# remove an item form list : remove(), discard()

my_set2 = {11, 12, 13, 14, 15, 20}
my_set2.remove(14)
print(my_set2)                                          # output : {11, 12, 13, 15, 20}
my_set2.discard(20)
print(my_set2)                                          # output : {11, 12, 13, 15}

# Union, Intersection, difference and symmetric difference.

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.union(b))                      # or print(a | b)            # output : {1, 2, 3, 4, 5, 6, 7, 8}
print(a.intersection(b))               # or print(a & b)            # output : {4, 5}
print(a.difference(b))                 # or print(a - b)            # output : {1, 2, 3}
print(a.symmetric_difference(b))       # or print(a ^ b)            # output : {1, 2, 3, 6, 7, 8}