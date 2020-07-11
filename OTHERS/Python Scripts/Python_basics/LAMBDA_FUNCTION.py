# lambda is anonymous function
# syntax of lambda
# lambda arguments_list : expression

# sum = lambda x, y : x+y
# print(sum(3, 4)) # return 7

# lambda is more powerful when it is used with map(),filter() and reduce()

# map() syntax:
# map(function, sequence) .First argument is function name and Second argument is sequence(e.g List,Tuple).map() applies
#                          function to all elements of sequence and it can apply to multiple sequence.
#                          To return map() as an list it is enclosed in list().

# c = [39.2, 36.5, 37.3, 38, 37.8]
# f = list(map(lambda x : (9/5)*x + 32, c))
# print(f)

# a = [1, 2, 3]
# b = [17, 12, 11, 10]
# c = [-1, -4, 5, 9]
#
# d = list(map(lambda x, y, z : x + y +z, a, b, c))
# print(d)

# filter()syntax :
# filter(function,sequence). Filter out all elements of sequence, for which function returns True.

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_fibonacci = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_fibonacci)
odd_fibonacci = list(filter(lambda x: x % 2 == 1, fibonacci))
print(odd_fibonacci)

# converting lambda to def function

# square_func = lambda x: x**2
#
# function_product = lambda F, m: lambda x: F(x)*m    #F,m are the arguments of outer function whereas x is argument of
#                                                   # inner function and expression F(x)*m is in inner function
#
# print(square_func(2))
#
# print(function_product(square_func, 3)(2))
square_func = lambda x: x ** 2


def function_product(F, m):  # returns inner, a function
    def inner(x):  # takes x, and closes over F and m from
        return F(x) * m  # outer scope, hence a closure

    return inner


print(square_func(2))
print(function_product(square_func, 3)(20))  # square_func and 3 are two arguments of function_product(F, m) and 20 is
# argument of inner function.
