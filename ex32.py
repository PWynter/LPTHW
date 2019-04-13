the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots,"]
change = [1, "pennies", 2, "dimes", 1, "quaters"]

# this kind of for loop goes through a list
for number in the_count:
# variable number is being assigned to each element of the_count
    print(f"This is count {number}")

for fruit in fruits:    
# variable fruits is assigned to each element of fruits
    print(f"A fruit of type {fruits}")

# also we can got through mixed lists too
# notice how we use {} since we dont know whats in it
for i in change:
# variable i is assigned to each elment in change
    print(f"I got {i}")

# we can build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
# varaible i is assigned to each element in range
    print(f"Adding {i} to the list.")
    # append is a function thats adds on to lists
    elements.append(i)

# now we can print them out too
for i in elements:
# variable i is assigned to each element og elements
    print(f"Element was: {i}")