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
		4 : 'thousand',
		3 : 'hundred'
			}
}

x = '101010101'
length = len(x)
i = 0
word = ''

def one():
	if x[i] == '1':
		return True
	else:
		return False


def zero():
	if x[i-1:i+1] == '00' or (length - i == 3 and x[i] == '0'):
		return True
	else:
		return False


while i <= length:
	if length % 2 == 1:			# length is odd
		if i % 2 == 0 and (length - i > 3):
			place = 'tens'
		elif (length - i) in (3, 1):
			place = 'ones'
		elif length - i == 2:
			place = 'tens'
		else:
			place = 'ones'
		if one() and ((length - i) in (13, 11, 9, 7, 5, 2)):
			word = word + ' ' + figure_to_word_dict[place][x[i:i+2]]
			i += 1
		else:
			word = word + ' ' + figure_to_word_dict[place][x[i]]
		if (length - i) in (12, 10, 8, 6, 4, 3) and not zero():
			word = word + ' ' + figure_to_word_dict['counting'][length - i]
		i += 1
	else:					# length is even
		if i % 2 == 0 and (length - i > 3):
			place = 'ones'
		elif (length - i) in (3, 1):
			place = 'ones'
		elif length - i == 2:
			place = 'tens'
		else:
			place = 'tens'
		if one() and ((length - i) in (13, 11, 9, 7, 5, 2)):
			word = word + ' ' + figure_to_word_dict[place][x[i:i+2]]
			i += 1
		else:
			word = word + ' ' + figure_to_word_dict[place][x[i]]
		if (length - i) in (12, 10, 8, 6, 4, 3) and not zero():
			word = word + ' ' + figure_to_word_dict['counting'][length - i]
		i += 1
	if length - i == 0:
		break


print(' '.join(word.split()))