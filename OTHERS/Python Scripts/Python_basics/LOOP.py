# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# sum = 0
# for element in numbers:
#     sum += element
# print('The sum is ', sum)

# print(list(range(0, 10, 2)))
i = 0
while i < 10:
    if i == 9:
        break
    if i == 6:
        i += 1
        continue # continue skip rest of loop code
    print(i)
    i += 1