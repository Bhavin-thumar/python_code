def ex33(a, b):
    i = 0
    numbers = []

    while i < a:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += b
        print("Numbers now :", numbers)
        print(f"At the end i is {i}")
    return numbers

calling_func = ex33(17, 4)
print("The number is : ")

for num in calling_func:
    print(num)
