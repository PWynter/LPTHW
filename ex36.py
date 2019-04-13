from sys import exit


def jamaica():
    print("Welcome to the sunshine island")
    print("Are you here to 'rent a rasta' ?")
    print("For the ganga? ")
    print("Or to relax? ")

    choice = input("> ")

    if "rent a rasta" in choice:
        print ("You didnt get a rasta but another local with a gift")
        dead("You contract syphallis and die.")
    elif "for the ganga" in choice:
        print("You arrive at the airport. And are met by a ganga farmer")
        print("Good times, the rest of the holiday is hazy")
    else:
        "relax" in choice
        print("Where do you want to go?")
        place = input("> ")
        print(f"Are you sure {place} is in Jamaica?")
        sure_place = input("Yes or No > ")

        if "no" in sure_place:
            print("Try again")
        else:
            print(f"Ok, enjoy Jamaica and {place}.")

def norway():
    print("Welcome to Norway!")
    print("Did you bring warm clothes?")

    warm_clothes = input("Yes or No? > ")

    if "no" in warm_clothes:
        dead("Back to the airport, you will freeze!")
        start()
    elif "yes" in warm_clothes:
        print("Good luck, you are on your own here.")
        exit(0)
    else:
        norway()

def dead(why):
    print(why, "Oh Well")
    exit()

def start():
    name = input("what your name? > ")
    print(f"{name} you are at the airport.")
    print(f"{name}, there is a door to your right and to your left.")
    print("Which do you take?")

    choice = input(">  ")

    if choice == "left":
        norway()
    elif choice == "right":
        jamaica()
    else:
        dead("You stumble around the room until you starve.")
   

start()