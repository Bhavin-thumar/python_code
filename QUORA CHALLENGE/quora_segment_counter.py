import quorachallenge

@quorachallenge.autotest('segment_counter')
def my_segment_counter(string):
	count = 0
	
	if not string:
		return count

	for index, current_letter in enumerate(string):
		try:
			next_letter = string[index + 1]
			if current_letter != next_letter:
				count +=1
		except IndexError:
			count += 1
	return count		