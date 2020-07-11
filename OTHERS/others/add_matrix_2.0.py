# matrix1 = [[1, -2, 3, 1], [-3, 4, 1], [2, 4], [3, 5]]
# matrix2 = [[2, -1, 2, 2], [0, -1, -2], [-1, -2], [3, 7]]
# matrix3 = [[-3, 3, -4, 3], [3, -3, -5], [0, -1], [-4, -5]]

def add(*iterables):
	return iterables

matrix = add([[1, -2, 3, 1], [-3, 4, 1], [2, 4], [3, 5]],
			 [[2, -1, 2, 2], [0, -1, -2], [-1, -2], [3, 7]],
			 [[-3, 3, -4, 3], [3, -3, -5], [0, -1], [-4, -5]])

result = []

k = 0
def create_sub_list():
	global k
	global j
	j = 0
	sub_list = []
	for _ in range(len(matrix[0][k])):
		sub_list.append(summation())
		j += 1
	k += 1
	return sub_list

def summation():
	sum = 0
	for i in range(len(matrix)):
		sum += matrix[i][k][j]
	return sum

for r in range(len(matrix[0])):
	result.append(create_sub_list())
print(result)