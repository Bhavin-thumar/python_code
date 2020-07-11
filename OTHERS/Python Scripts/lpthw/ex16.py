from sys import argv

script, filename = argv

print(f"We are going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit Return.")

input("?")

print("Opening the file....")
target = open(filename,'w')

print("Truncating the file. Goodbye.")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write this in file.")

edited_file = f"{line1}\n{line2}\n{line3}"
target.write(edited_file)
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally we closeit.")
target.close()
