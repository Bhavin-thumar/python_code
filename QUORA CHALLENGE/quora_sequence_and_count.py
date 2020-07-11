import quorachallenge

@quorachallenge.autotest('sequence_and_count')
def count_sequence(string):
	if not string:
		return [[None, 0]]

	mylist = []
	count = 1
	for index, current_letter in enumerate(string):
		try:
			next_letter = string[index + 1]
			if current_letter != next_letter:
				mylist.append([current_letter, count])
				count = 0
			count += 1
		except IndexError:
			previous_letter = string[index - 1]
			if current_letter == previous_letter:
				mylist.append([current_letter, count])
			else:
				mylist.append([current_letter, 1])

	return mylist