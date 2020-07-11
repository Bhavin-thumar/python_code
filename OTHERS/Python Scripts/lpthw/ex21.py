def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subrtact(a, b):
    print(f"Subracting {a} - {b}")
    return a -b

def multiply(a, b):
    print(f"Multipling {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print("let's do some math using functions.")

age = add(30, 5)
height = subrtact(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age : {age}, Height : {height}, Weight : {weight}, IQ : {iq}")

# A puzzlw for extra credit, type it in anyway.
print("here is puzzle.")

what = add(age, subrtact(height, multiply(weight, divide(iq, 2))))

print("That become :", what, "Can you do it by hand.")
