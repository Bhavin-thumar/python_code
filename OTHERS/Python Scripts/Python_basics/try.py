#
# def slicing(word):
#     # print(word)
#     if len(word) == 1:
#         # break
#         return word
#     return word + slicing(word[:len(word)-1])
#
# print(slicing('abc'))
#
# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num-1)

# print(factorial(5)
my_list = ['0', '1', '2', '3', '4']
from itertools import permutations

print(permutations([my_list]))
x = list(permutations([my_list]))
print(len(x))

for i in x:
    print("".join(i))