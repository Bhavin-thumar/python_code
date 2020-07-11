# create mapping of state to abbreviation

states = {
        'Oregon' : 'OR',
        'Florida' : 'FL',
        'California' : 'CA',
        'New York' : 'NY',
        'Michigan' : 'MI'
}

cities = {
    'CA' : 'San Fransisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'
}

# add more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# print out some cities
print('-' * 10)
print("NY State has :", cities['NY'])
print("OR state has :", cities['OR'])

#print sone states
print('-' * 10)
print("Michigan abbreviation is :", states['Michigan'])
print("Florida abbreviation is :", states['Florida'])

# do it by using state then cities dict
print('-' * 10)
print("Michigan has :", cities[states["Michigan"]])
print("Florida has :", cities[states["Florida"]])

#print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in states
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')
print("State value :", state)

if not state:
    print("Sorry, no Texas")

# get a city with default value
city = cities.get('TX', 'Does not Exist.')
print(f"The city for state 'TX' is : {city}")
