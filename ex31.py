
door = (input("""You enter a dark room with two doors.
Do you through door #1 or door #2? >> """))

if door == "1":
    print("There is a giant bear eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(">> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare in the endless abyss at Cthulu's ret.")
    print("1. Blueberries.")
    print("2. Yellow Jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input(">> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of mud.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die.") 