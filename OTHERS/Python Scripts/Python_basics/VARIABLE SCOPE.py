# Note 1: Variable declare outside of function can be access inside of function[e.g scope()]
# Note 2 :Variable declare outside of function cannot modify it inside of function directly [e.g scope2()]cont. Note 2_1
# Note 2_1 : To modify it variable should be declared with 'global' keyword inside of function[e.g scope2_1]
# Note 3:Variable declare inside of function is Local Variable and it cannot be access outside of function[e.g scope3()]
# Note 4 : Calling Variable follows LEGB(Local,Enclosed function,Global and Built in) rules i.e it first look for local
#           variable if not found then look in enclosed function, then Global variable and then built ins.[e.g foo()]
# Note 5 : Nonlocal variable is used only in nested function. It copy value to variable in upper order function
#          Global variable in nested function copy value to variable which is outside of whole function.[e.g foo()]

# x = 10

# def scope():
#     print("x inside :", x)

# scope()
# print("x outside :", x)

# gives output :
# x inside : 10
# x outside : 10

# x = 10
# def scope2():
#     x = x*2
#     print("x inside :", x)

# scope2()

# x = 10
# def scope2_1():
#     global x
#     x = x*2
#     print("x inside :", x)

# scope2_1()


# def scope3():
#     y = 11
#     print(y)

# scope3()
# print(y) gives error : Note: 3

x = 15
def foo():
    x = 20

    def bar():
        nonlocal x
        # global x
        x = 25
        print("Value in bar() :", x)

    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)


foo()
print("x in main : ", x)