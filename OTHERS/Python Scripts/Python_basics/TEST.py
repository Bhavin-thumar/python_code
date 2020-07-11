list1 = [1, 4, 2, 5, -2, 10, 9, 8, 7]
i = 0
e = 1
while i <= len(list1)-1:
    if e >= len(list1):
        i += 1
        # print(f'the value of i in first if : {i}')
        e = i + 1
        # print(f'the value of e in first if: {e}')
    if i >= len(list1)-1:
        break
    if list1[i] > list1[e]:
        temp = 0
        temp = list1[i]
        list1[i] = list1[e]
        list1[e] = temp
        # print(f'the value of list {i} : {list1[i]}')
        # print(f'the value of list {e} : {list1[e]}')
        # print(list1)
        e += 1
        # print(f'the value of e in second if : {e}')
    else:
        e += 1
        # print(f'the value of e in else : {e}')
print(list1)