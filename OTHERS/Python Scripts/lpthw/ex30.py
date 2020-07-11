people = 30
cars = 40
trucks = 15


if cars > people:
    print("we should take the cars")
elif cars < people:
    print("we should not take the cars")
else:
    print("We can't decide")

if trucks > cars or people > trucks:
    print("That's too many truks.")
elif trucks < cars:
    print("Maybe we should take truks.")
else:
    print("we still can't decide")

if people > trucks:
    print("Alright lets just take truks.")
else:
    print("Fine, let's stay at home.")
