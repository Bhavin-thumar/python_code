# syntax to define function
# def function_name(arguments):
#     """doc string"""
#     statement
def greet(name,msg):
    """this function greet person
    with name"""
    print("hello", name, ',', msg)

# greet("monica","hi there") gives output: hello monica , hi there

# greet("monica") gives error 1 argument missing : msg
# greet() gives error 2 argument missing

def greet2(name,msg="good morning"):
    """this function greet person
    with name"""
    print("hello", name, ',', msg)

# greet2("kate") gives output : hello kate , good morning
# greet2(name="bruce","hi there") gives syntax error as positional argument follows keyword arguments.

def greet3(*args, **kwargs):
    """this function takes multiple positional arguments as *args and store them as tuple
        and multiple keyword arguments as **kwargs and store them as dictionary"""
    print(args, kwargs)
    for i in args:
        print("hello", i)
    
greet3('monica', 'luke', 'steve', 'john', age = 22, city = 'sanjose' )
#      gives output ('monica', 'luke', 'steve', 'john'){'age': 22, 'city': 'sanjose'}
#                    hello monica
#                    hello luke
#                    hello steve
#                    hello john