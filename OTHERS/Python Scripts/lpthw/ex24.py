print("let's practice everything.")
print("you\ 'd need to know \'bout escapes with \\ that do:"")
print('\n newlines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the need of lovely
nor comprehend passion from intuition
and requries an explannation
\n\t\t where there is none.
"""

print("---------------")
print(poem)
print("---------------")


five = 10 - 2 + 3 -6
print(f"This would be five : {five}")

def secret_formula(started):
    jelly_beans = started * 100
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember there is another way to format stringself.
print("What a starting point of : {}".format(start_point))
# its just like f stringself
print(f"we'd have {beans} beans, {jars} jars and {crates} crates.")

start_point = start_point / 10

print("we can also do that this way:")
formula = secret_formula(start_point)
#this ia an easy way to apply a list to format stringself
print("we'd have {} beans, {} jars, and {} crates.".format(*formula))
