# list are mutable i.e change
# empty list
list1 = []

# list of integers
list2 = [1, 2, 3]

# list with mixed integers
list3 = [1, "hello", 2.5]

# nested list
list4 = [1, 2, [3, 4, 5], 'python']

# list index and slicing
print(list4[0])                      # output : 1
print(list4[2])                      # output : [3, 4, 5]
print(list4[2][1])                   # output : 4
print(list4[3][3])                   # output : h
print(list4[:])                      # output : [1, 2, [3, 4, 5], 'python']
print(list4[1:3])                    # output : [2, [3, 4, 5]]
print(list4[-2:])                    # output : [[3, 4, 5], 'python']
print(list4[:-2])                    # output : [1, 2]

# changing and adding list items
odd = [2, 4, 6, 8]
odd[0] = 1                          # output : [1, 4, 6, 8]
print(odd)
odd[1:4] = [3, 5, 7]                # output : [1, 3, 5, 7]
print(odd)

odd.append(9)                       # to add at end of list
print(odd)                          # output : [1, 3, 5, 7, 9]
odd.extend([11, 13, 15])            # to extend list
print(odd)                          # output : [1, 3, 5, 7, 9, 11, 13, 15]
print(odd + [17, 19, 21])           # temporary add to list output : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
print(odd)                          # output : [1, 3, 5, 7, 9, 11, 13, 15]
print("hi" * 4)                     # output : hihihihi

# insert item in list
even = [2, 6, 8]
even.insert(1, 4)                   # to insert any item at desired index. syntax insert(index_position, item)
print(even)                         # output : [2, 4, 6, 8]

# delete or remove item from list
print(odd)                          # output : [1, 3, 5, 7, 9, 11, 13, 15]
del odd[5]                          # delete item at index 5
print(odd)                          # output : [1, 3, 5, 7, 9, 13, 15]
del odd[1:3]                        # delete item from index 1 to 2
print(odd)                          # output : [1, 7, 9, 13, 15]
del odd                             # delete entire list
# print(odd)                          # error 'odd' not defined

# remove elements from list
list4 = [1, 2, 5, 'python', 6, 7, 8, 2]
# list4.remove(1)                   # remove given item from list not item at that index no.
# print(list4)                      # output : [2, [3, 4, 5], 'python']
print(list4.pop(-1))                # remove an item at the given index, default index is -1.
# print(list4)
# list4.clear()                     # clear list

# sort, index and count
# print(list4.index(1))               # return the index value of given item
# print(list4)
# print(list4.count(2))             # count the given value in list
# print(list4.sort())               # sort list
# print(sorted(list4))              # sort list