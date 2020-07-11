print("""You enter a dark room with two doors
Do you go through door #1 or door #2""")

door = input("> ")

if door == "1":
    print("There is giant beer here eating cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream the bear")

    bear = input("> ")

    if bear == "1":
        print("The beer eats your face off. Good job")
    elif bear == "2":
        print("The beer eats your legs off. Good job")
    else:
        print(f"well, doing {bear} is probably better")
        print("Bear runs away")

elif door == "2":
    print("you stare into endless at retina")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives")
        print("Good job")
    else:
        print("The insanity rots your eyes into pool")
        print("Good job")

else:
    print("You stumble around and fall on knife and die. Good job")
