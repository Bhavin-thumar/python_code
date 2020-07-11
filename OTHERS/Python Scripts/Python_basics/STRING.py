# string are immutable i.e cannot change/add/delete its elements.

# indexing and slicing are same as list/tuple.

# iterating and membership test same as list/tuple.

# format() method for formatting string. We can use positional arguments or keyword arguments to specify order.

default_order = "{}, {} and {}".format('John', 'Bill', 'Sean')          # default implicit order
print('\n------Default Order------')                                    # output : ------Default Order------
print(default_order)                                                    # output : John, Bill and Sean

positional_order = "{1}, {0}, and {2}".format('John', 'Bill', 'Sean')   # order using positional argument
print('\n------Positional Order----')                                   # output : -------Positional Order------
print(positional_order)                                                 # output : Bill, John and Sean

keyword_order = "{s}, {b}, and {j}".format(j = 'John', b = 'Bill', s = 'Sean')   # order using keyword_order
print('\n-------Keyword Order------')                                            # output : --------keyword Order------
print(keyword_order)                                                             # output : Sean, Bill and John

print("\nRound off is : {0:.2f}\n".format(100/3))                       # Output : 33.33
x = 3.1456789
print('the value of x is : %.2f\n' %x)                                  # Output : 3.14
print('the value of x is : %.4f\n' %x)                                  # Output : 3.1457

# lower(), upper(), join(), split(), find(), replace()

print("PrOgRaMiZ".lower())                                              # Output : programiz
print("PrOgRaMiz".upper())                                              # Output : PROGRAMIZ
print("This will split word.".split())                            # Output type list : ["This", "will", "split", "word"]
print(" ".join(['This', 'will', 'join', 'word']))                 # Output : This will join word
print('happy new year'.find('ye'))                                      # Output : 10
print('happy new year'.replace('happy', 'brilliant'))                   # Output : brilliant new year