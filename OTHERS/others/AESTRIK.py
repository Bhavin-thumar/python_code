' Uses of * and ** '

'1. * and ** to pass arguments to function '
'2. * and ** to capture arguments passed into function'
'3. * to accept keyword-only arguments'
'4. * to capture items during tuple unpacking'
'5. * to unpack iterables into list/tuple'
'6. ** to unpack dictionaries into other dictionaries'

numbers = [2, 1, 3, 4, 7]
more_numbers = [*numbers, 11, 18]

print(more_numbers)
# passing all items in more_numbers to print function call as separate arguments
print(*more_numbers)
'it is same as print(more_numbers[0],more_numbers[1],more_numbers[2],more_numbers[3],more_numbers[4]'
'more_numbers[5],more_numbers[6])'


def transpose_list(*list_of_lists):
	return [
        list(row)
        for row in zip(*list_of_lists)
    ]


print(transpose_list([1, 4, 7], [2, 5, 8], [3, 6, 9]))

*city, day, time = ['san jose', 'mon', '19:00']
print(*city)
print(day)
print(time)

date_info = {'year': '2020', 'month': '01', 'day': '01'}
filename = '{year}-{month}-{day}.txt'.format(year = '2020', month = '01', day = '01')

print(filename)
print(*date_info)
print(tuple(date_info.keys())[0], tuple(date_info.keys())[1], tuple(date_info.keys())[2])
