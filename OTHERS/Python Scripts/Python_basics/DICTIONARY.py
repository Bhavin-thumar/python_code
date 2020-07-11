# It is unordered collection of items. A dictionary has Key: Value pair.
# Dictionary are optimized to retrieve value when keys are known.
# Dictionary is created by putting items in {}. Syntax of dictionary - {Key : Value}
# While Value can be of any type and can repeat, Keys must be of immutable type(string, number of tuple with immutable
# elements) and must be unique.


# accessing keys, values and items.

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.items())                          # output : dict_items([(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])
print(squares.keys())                           # output : dict_keys([1, 2, 3, 4, 5])
print(squares.values())                         # output : dict_values([1, 4, 9, 16, 25])

cubes = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
for i in cubes.values():
    print(i)


# Dictionary comprehension

table_2 = {x: x * 2 for x in range(15) if x % 2 == 0}
print(table_2)                  # output : {0: 0, 2: 4, 4: 8, 6: 12, 8: 16, 10: 20, 12: 24, 14: 28}


# nested dictionary

people = {1: {'name': 'John', 'age': '27', 'sex': 'male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'female'}
    }
print(people.keys())            # output : dict_keys([1, 2])
print(people.values())#([{'name': 'John', 'age': 27, 'sex': 'male'}, {'name': 'Marie', 'age': 22, 'sex': 'female'}])
print(people.items())   # output : dict_items([(1, {'name': 'John', 'age': 27, 'sex': 'male'}),
                                            #  (2, {'name': 'Marie', 'age': 22, 'sex': 'female'})])

# accessing elements from nested dictionary.
print(people[1]['age'])             # output : 27
print(people[2]['name'])            # output : 'Marie'

# Adding/Deleting elements in dictionary.

people[3] = {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}
people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}

print(people)

# Iterating through nested dictionay

for people_id, people_info in people.items():
    print("\npeople id ", people_id)
    for key in people_info:
        print(key +':', people_info[key])
