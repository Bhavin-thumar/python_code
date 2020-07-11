# list membership test
list4 = [1, 2, [3, 4, 5], 'python']
# print(1 in list4)                   # output : True
# print(3 in list4)                   # output : False

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# i want "n" for each 'n' in nums
nums_1 = [x
          for x in nums]
print(nums_1)

# i want n+n for each 'n' in nums
nums_2 = [x+x
          for x in nums]
print(nums_2)
nums_21 = list(map(lambda x: x+x, nums))            # alternate way using map function
print(nums_21)

# i want 'n' for each 'n' in nums if 'n' is even
nums_3 = [x
          for x in nums
          if x % 2 == 0]
print(nums_3)
nums_4 = list(filter(lambda x: x % 2 == 0, nums))       # alternate way using filter function
print(nums_4)

# I want a (letter,num) pair for each letter in 'abcd' and each number in '0123'
nums_5 = [(x, y)
          for x in 'abcd'
          for y in '0123']
print(nums_5)
""" output :[('a', '0'), ('a', '1'), ('a', '2'), ('a', '3'), ('b', '0'), ('b', '1'), ('b', '2'), ('b', '3'), ('c', '0'),
           ('c', '1'), ('c', '2'), ('c', '3'), ('d', '0'), ('d', '1'), ('d', '2'), ('d', '3')]"""