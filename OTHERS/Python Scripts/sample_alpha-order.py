with open(r'C:\Users\hardip thummar\Documents\Python Scripts\alpha_order.txt', mode='r') as f:
	main_list = []
	for line in f:
		new_list = []
		*city, day, time = line.split()
		new_list.append(' '.join(city))
		new_list.append(day)
		new_list.append(time)
		main_list.append(new_list)
	print(sorted(main_list, key= lambda x : x[0]))