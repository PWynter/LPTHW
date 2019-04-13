people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! the world is doomed")

if people > cats:
    print("Not many cats!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5
#dogs = dogs + 5

print(f"Number of dogs now: {dogs}")

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs")

if people == dogs:
    print("People are dogs")