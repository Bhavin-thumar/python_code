dialogue = "My name is bond james bond"
vowels = 'aeiou'
split_dialogue = dialogue.split()
dialogue_without_vowels = ""

for i in dialogue:
    if i in vowels:
        continue
    dialogue_without_vowels += i

print(dialogue_without_vowels)
print(split_dialogue)
print(" ".join(split_dialogue))

# if True:
#     print("Hello")
# if False:
#     print("Me too.")
# elif False:
#     print("Hello too.")
# elif False:
#     print("Hi there.")
# else:
#     print("Bye thers.")


# def add(a):
#     def double_adder(b, c):
#         return b + c
#     return double_adder
#
# x = add(5)(10, 20)
# # print(x)
# def factorial(num):
#     if num == 1:
#         return 1
#     return num * factorial(num-1)
#
# print(factorial(5))
# #
# x = 'abcde'
# print(x[:1])
# print(x[:2])
# print(x[:3])
# print(x[:4])
# print(x[:5])
#
# x = 'abc'
# for i in range(len(x)+1):
#     print(x[i:])
