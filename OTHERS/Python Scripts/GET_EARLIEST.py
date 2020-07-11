def converter(x):
	month, day, year = x.split('/')
	convert_x = int(year + month + day)
	return convert_x


def get_earliest(*date):
	date_converted = list(map(converter, date))
	return date[date_converted.index(min(date_converted))]


print(get_earliest('02/30/1920', '01/01/2002', '02/20/1972', '03/29/1945'))