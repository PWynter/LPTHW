a = 0
numbers = []

while a < 6:
    print(f"At the top A is {a}")
    numbers.append(a)

    a = a + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom, a is {a}")


print("The numbers: ")

for num in numbers:
    print(num)


print("printing the list now:", numbers)