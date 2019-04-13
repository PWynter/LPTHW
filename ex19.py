#define the function cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man thats enough for a party!")
	print("Get a blanket.\n") # blank line after full stop

# prints below string
print("We can just give the function numbers directly:")
#gives the function values
cheese_and_crackers(20, 30)

#prints string
print("OR, we can use variables from our script:")
#creates variables 
amount_of_cheese = 10
amount_crackers = 50

#call function with using new arguments
cheese_and_crackers(amount_of_cheese, amount_crackers)

#print string
print("We can even do math inside too:")
#call function with added arguments
cheese_and_crackers(10 + 20, 5 + 6)

#print string
print("And we can combine the two, variables and math:")
#call function using temporary variables as arguments then adding on to that
cheese_and_crackers(amount_of_cheese + 100, amount_crackers + 1000)