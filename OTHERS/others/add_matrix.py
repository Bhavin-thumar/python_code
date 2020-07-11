# matrix1 = [[1, -2, 3, 1], [-3, 4, 1]]
# matrix2 = [[2, -1, 2, 2], [0, -1, -2]]
# matrix3 = [[-3, 3, -4, 3], [3, -3, -5]]

def add(*iterables):
	zipped = zip(*iterables)
	return [
			list(map(sum, zip(*sub_list))) 
			for sub_list in zipped
		]

obj = add([[1, -2, 3, 1], [-3, 4, 1], [2, 4], [3, 5]],
    	  [[2, -1, 2, 2], [0, -1, -2], [-1, -2], [3, 7]],
    	  [[-3, 3, -4, 3], [3, -3, -5], [0, -1], [-4, -5]])

print(obj)

# result = [list(map(sum, zip(*sub_list))) for sub_list in zipped]
# print(list(zipped))
# result = []
# for a in zipped:
# 	result.append(list(map(sum, zip(*a))))

# print(result)
# main_sub_list = []
# for i,row in enumerate(zipped):
# 	sub_list = []
# 	for e,column in enumerate(row):
# 		sub_list.append(column)
# 	main_sub_list.append(zip(*sub_list))

# summation = []
# for r in main_sub_list:
# 	summation.append(list(map(sum, r)))

# print(summation)