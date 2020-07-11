import quorachallenge

@quorachallenge.autotest('run_length_encoder')
def run_length_encode(string):
	string_copy = ''

	for index, current_letter in enumerate(string):
		if index != len(string)-1:
			next_letter = string[index + 1]
			if current_letter != next_letter:
				string_copy += current_letter + ','
			else:
				string_copy += current_letter
		else:
			string_copy += current_letter

	mylist = string_copy.split(',')

	output_string = ''
	for item in mylist:
		if len(item) < 3:
			output_string += item
		elif len(item) >= 3 and len(item) <= 9:
			output_string += item[0] + str(len(item))
		else:
			remainder = len(item) % 9
			quotient = int((len(item) - remainder) / 9)
			for _ in range(quotient):
				output_string += item[0] + '9'
			if remainder > 0 and remainder < 3:
				for _ in range(remainder):
					output_string += item[0]
			elif remainder >= 3:
				output_string += item[0] + str(remainder)

	return output_string