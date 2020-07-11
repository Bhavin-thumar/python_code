the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarter']

# this first kind of for loop goes through list
for number in the_count:
    print(f"This is count {number}")

# same as abouve
for fruit in fruits:
    print(f"A fruit of type : {fruit}")

# also we can go through mixed lists too
for i in change:
    print(f"I got {i}")

#we can also build list first start with an empty one
elements = []

# then use range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list")
    elements.append(i)

# now we can print them out # Too
for i in elements:
    print(f"elements was {i}")
