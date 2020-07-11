x = '3000 30 30 3'

str_x = sorted(list(map(lambda x : str(x), x.split())))

max_digit = 0
for e in str_x:
	if len(e) > max_digit:
		max_digit = len(e)

num_x = list(map(lambda x : int(x), str_x))

i = 0
for e in str_x:
	num_x[i] = num_x[i] * pow(10, (max_digit-len(e)))
	i += 1

zip_x_y = zip(str_x,num_x)

sorted_x_y = sorted(list(zip_x_y), key=lambda x : x[1], reverse=True)

largest_number = ''

for (i,j) in sorted_x_y:
	largest_number += i

print(largest_number)