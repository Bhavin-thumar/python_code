# this line is added in github
# this line is added in local repository
# this line is added after cloning from D: drive
def max_recur(lst):

    def helper(i, x):

        if i == len(lst):
            return x
        if lst[i] > x:
            x = lst[i]

        return helper(i + 1, x)

    return helper(1, lst[0])


lst = [3, 7, 2, 5]
print(max_recur(lst))
