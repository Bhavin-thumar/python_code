def combi(lst, count, s = ''):

    if count == 0:
        print(s)

    else:
        count -= 1
        counter = 1
        for i in lst:
            new_s = s +i
            new_lst = lst[counter : ]
            counter += 1
            combi(new_lst, count, new_s)


lst = ['1','2','3','4','5', '6', '7', '8', '9']

combi(lst, 4)
