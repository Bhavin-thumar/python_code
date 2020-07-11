def create_sub_list():
	sub_list = []
	*city, day, time = line.split()
	sub_list.append(' '.join(city))
	sub_list.append(day)
	sub_list.append(time)
	return sub_list


def addto_main_list():
	return main_list.append(create_sub_list()) 


main_list = []

with open(r'C:\Users\hardip thummar\Documents\Python Scripts\alpha_order.txt', mode='r') as f:
	for line in f:
		create_sub_list()
		addto_main_list()
	
print(sorted(main_list, key=lambda x : x[0]))