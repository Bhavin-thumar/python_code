x = 1254

for i in range(x, 0, -1):
	list_x = [digit for digit in str(i)]
	if list_x == list_x[::-1]:
		print(f'Nearest palindrome of {x} is : {i}')
		break