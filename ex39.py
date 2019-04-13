states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA' : "San Francisco",
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

print(type(states))
print(states)
print(type(cities))
print(cities)

cities['NY'] = "New York"
cities['OR'] = "Portland"

print(cities,"\n\n")

print('-' * 10)
print("NY State is:", cities['NY'])
print("OR State is:", cities['OR'])
print('-' * 10)

print('-' * 10)
print("Michigan's abreviation is:", states['Michigan'])
print(f"Florida's abreviation is:" states['Florida'])
print('-' * 10)


print('-' * 10)
print("Michigan's city is:", cities['MI'])
print(f"Florida's city is:" cities['FL'])
print('-' * 10)
print("\n\n")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated : {abbrev}")
print('-' * 10, "\n\n")

print('-' * 10)
for state, abbrev in states.items():
    print(f" The state {state} is abbreviated {abbrev}")
print('-' * 10, "\n\n")

print('-' * 10)
for abbrev, city in cities.items():
    print(f" the state {abbrev} has {city} as a city !")
print('-' * 10, )   


states['Texas'] = 'TX'
tx_city = str(input("Please enter the city for Texas: "))
cities['TX'] = tx_city

state = states.get('Texas')

if not state:
    print("Sorry, no Texas")
else:
    print("Of Course Texas !")