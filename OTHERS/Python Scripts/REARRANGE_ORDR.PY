x = '3 2 0 1'
y = dict(enumerate(x.split()))
new_list = [0] * len(y)

listvalues = list(y.values())

for i in y:
	new_list[listvalues.index(str(i))] = y[i]

for el in new_list:
	print(el, end=' ')