from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input(">")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, your're not greedy, you win!") 
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here,")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    print("take honey ?" "taunt bear ?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "open door" and bear_moved:
            gold_room
        else:
            print("I got no idea what that means.")
            bear_room()

def cthulu_room():
    print("Here you see the great city of Cthulu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or head in?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head in" in choice:
        start()
        dead("Well that was tasty")
    else:
        cthulu_room

def dead(why):
    print(why, "Good job")
    exit()

def start():
    print("You are in a dark room.")
    print("There is a door to your right and to your left.")
    print("Which do you take?")

    choice = input(">  ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")

start()