from sys import argv     # missing

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()                        # variable 'height' missing
print("How much do you weigh?", end=' ') # ) missing
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

txt = open(filename)             # filename written as filenme

print("Here's your file {filename}:")
print(txt.read())                 # txt written as tx

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())             # .read() as _read()


print('Let\'s practice everything.')            # \ missing
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')
                                    # above lines should be in one line not two.
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")                 # " MISSING
print(poem)
print("--------------")                 # " MISSING


five = 10 - 2 + 3 - 6           # 6 missing
print(f"This should be five: {five}")    # ) missing

def secret_formula(started):            # : missing
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100                   # / missing
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # crates missing

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)   # start_point written as startpoint
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30                              # cats written as cates
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")        # () missing

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:                                   # : missing
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:                                  # : missing
    print("People are less than or equal to dogs.")  # " MISSING


if people == dogs:                                  # == WRITEEN AS =
    print("People are dogs.")
