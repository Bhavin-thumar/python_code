class NumbertoWords:
	def __init__(self):
		self.dict1to19 = {0 : '',
			1 : 'One',
			2 : 'Two',
			3 : 'Three',
			4 : 'Four',
			5 : 'Five',
			6 : 'Six',
			7 : 'Seven',
			8 : 'Eight',
			9 : 'Nine' ,
            10 : 'Ten',
			11 : 'Eleven',
			12 : 'Twelve',
			13 : 'Thirteen',
			14 : 'Fourteen',
			15 : 'Fifteen',
			16 : 'Sixteen',
			17 : 'Seventeen',
			18 : 'Eighteen',
			19 : 'Nineteen'}

		self.dictfrom20 = {
            0 : '',
            2 : 'Twenty',
			3 : 'Thirty',
			4 : 'Forty',
			5 : 'Fifty',
			6 : 'Sixty',
			7 : 'Seventy',
			8 : 'Eighty',
			9 : 'Ninety'
						}

		self.dict_divisor = {
			    10 : '',
			    100 : 'hundred',
			    1000 : 'thousand',
			    100000 : 'lac',
			    10000000 : 'crore',
			    1000000000 : 'arab',
			    100000000000 : 'kharab'
					}

		self.divisor_list = list(self.dict_divisor.keys())


	def length(self,n):
	    mydict = {
	        1 : 1,
	        2 : 1,
	        3 : 2,
	        4 : 3,
	        5 : 3,
	        6 : 4,
	        7 : 4,
	        8 : 5,
	        9 : 5,
	        10 : 6,
	        11 : 6,
	        12 : 7,
	        13 : 7,
	        14 : 8,
	        15 : 8
	    }
	    result = mydict[len(str(n))]
	    return result


	def number_name(self, num):
	    name_list = []
	    number = num
	    get_length = self.length(number)
	    for divisor in reversed(self.divisor_list[: get_length]):

	        quotient = number // divisor

	        if quotient > 19 and divisor != 100 and divisor != 10:
	            tenth_place_digit = quotient // 10
	            unit_place_digit = quotient % 10
	            name_list.append(self.dictfrom20[tenth_place_digit])
	            name_list.append(self.dict1to19[unit_place_digit])
	            name_list.append(self.dict_divisor[divisor])

	        else:
	            if quotient <= 19 and divisor != 10:
	                name_list.append(self.dict1to19[quotient])
	                if quotient != 0:
	                    name_list.append(self.dict_divisor[divisor])

	        if divisor == 10:
	            if number > 19:
	                tenth_place_digit = number // 10
	                unit_place_digit = number % 10
	                name_list.append(self.dictfrom20[tenth_place_digit])
	                if unit_place_digit != 0:
	                    name_list.append(self.dict1to19[unit_place_digit])
	            else:
	                name_list.append(self.dict1to19[number])

	        number = number - (quotient * divisor)

	        if number == 0:
	            break

	    return ' '.join(name_list)



	def write_number_name(self, start, end=None):
		if end is None:
			end = start
		with open(r'C:\Users\hardip thummar\Desktop\number_name.txt', 'w') as f:
			for num in range(start, end + 1):
				line = f'{num}-{self.number_name(num)}\n'
				f.write(f'{line}')
		print('Done')



mynumbers = NumbertoWords()
print(mynumbers.number_name(11010))
