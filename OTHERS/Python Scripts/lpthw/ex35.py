from sys import exit

def gold_room():
    print("this room is full of gold. How much do you take.")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print("Nice you are not greedy, you win.")
    else:
        dead("You are greedy bastard.")


def bear_room():
    print("THere is bear here.")
    print("The bear has a bunch of honey.")
    print("the fat bear is in front of another door.")
    print("How are you going to move the bear.?")
    bear_moved = False

    while True:
        choice = input('> ')

        if choice == "take honey":
            dead("the bear looks at you then slaps your face off.")
        elif choice =="taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("the bear get pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I have no idea what that means.")

def cthulhu_room():
    print("here are some great evil cthulhu.")
    print("He, it whatever stares at you and you go insane.")
    print("Do you flee for your life or eat yur head.?")

    choice = input('> ')

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty.")
    else:
        cthulhu_room()

def dead(why):
    print(why, "good Job.!")
    exit(0)

def start():
    print("You are in dark room.")
    print("There is door to open right or left.")
    print("Which one do you take.?")

    choice = input('> ')

    if choice == 'left':
        bear_room()
    elif choice == 'right':
        cthulhu_room()
    else:
        dead("you stumble around room until you starve.")

start()
