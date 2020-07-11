figure_to_word_dict = {
		'ones' : {
			'0' : '',
			'1' : 'One',
			'2' : 'Two',
			'3' : 'Three',
			'4' : 'Four',
			'5' : 'Five',
			'6' : 'Six',
			'7' : 'Seven',
			'8' : 'Eight',
			'9' : 'Nine' 
				},
		'tens' : {
			'0' : '',
			'10' : 'Ten',
			'11' : 'Eleven',
			'12' : 'Twelve',
			'13' : 'Thirteen',
			'14' : 'Fourteen',
			'15' : 'Fifteen',
			'16' : 'Sixteen',
			'17' : 'Seventeen',
			'18' : 'Eighteen',
			'19' : 'Nineteen',
			'2' : 'Twenty',
			'3' : 'Thirty',
			'4' : 'Forty',
			'5' : 'Fifty',
			'6' : 'Sixty',
			'7' : 'Seventy',
			'8' : 'Eighty',
			'9' : 'Ninety' 
				},
		'counting' :{
			12 : 'Kharab',
			10 : 'Arab',
			8 : 'Crore',
			6 : 'Lac',
			4 : 'Thousand',
			3 : 'Hundred'
				}
	}

x = '72345454'
length = len(x)
i = 0
word = ' '

def one():
	if x[i] == '1':
		return True
	else:
		return False


def zero():
	if x[i-1:i+1] == '00' or (position_from_right() == 3 and x[i] == '0'):
		return True
	else:
		return False


def position_from_right():
	return length - i


def go_to_next_digit():
	global i
	i += 1
	return i


def end_of_string():
	if position_from_right() == 0:
		return True
	else:
		return False 

def ones_tens():
	if position_from_right() in (14, 12, 10, 8, 6, 4 ):
		return 'ones' 
	elif position_from_right() in (3, 1):
		return 'ones'
	elif position_from_right() in ( 2, ):
		return 'tens'
	elif position_from_right() in (15, 13, 11, 9, 7, 5 ):
		return 'tens'

def pronounce_and_join_word_for_digit_1():
	global word
	word = word + ' ' + figure_to_word_dict[place][x[i:i+2]]
	return word

def pronounce_and_join_word_for_current_digit():
	global word
	word = word + ' ' + figure_to_word_dict[place][x[i]]
	return word


def add_numbering_system():
	global word
	word = word + ' ' + figure_to_word_dict['counting'][position_from_right()]
	return word


while i <= length:
	place = ones_tens()
	if one() and (position_from_right() in (15, 13, 11, 9, 7, 5, 2)):
		pronounce_and_join_word_for_digit_1()
		go_to_next_digit()
	else:
		pronounce_and_join_word_for_current_digit()
	if position_from_right() in (14, 12, 10, 8, 6, 4, 3) and not zero():
		add_numbering_system()
	go_to_next_digit()

	if end_of_string():
		break

print(' '.join(word.split()))





