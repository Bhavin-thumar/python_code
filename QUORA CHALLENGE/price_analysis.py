import quorachallenge
from datetime import date,timedelta

# prices = [('2020-01-16', 203), ('2020-01-17', 208), ('2020-01-20', 208), ('2020-01-21', 203), ('2020-01-22', 196), ('2020-01-23', 203), ('2020-01-24', 200), ('2020-01-27', 209), ('2020-01-28', 208), ('2020-01-29', 206), ('2020-01-30', 196), ('2020-01-31', 202), ('2020-02-03', 201), ('2020-02-04', 191), ('2020-02-05', 185), ('2020-02-06', 179), ('2020-02-07', 188), ('2020-02-10', 180), ('2020-02-11', 181), ('2020-02-12', 190), ('2020-02-13', 195), ('2020-02-14', 186), ('2020-02-17', 190), ('2020-02-18', 184), ('2020-02-19', 181), ('2020-02-20', 186), ('2020-02-21', 190), ('2020-02-24', 193), ('2020-02-25', 194), ('2020-02-26', 200), ('2020-02-27', 195), ('2020-02-28', 188), ('2020-03-02', 182), ('2020-03-03', 180), ('2020-03-04', 184), ('2020-03-05', 175)]

@quorachallenge.autotest('stock_analysis')
def stock(prices):
	try:
		sorted_list = sorted(prices,key = lambda x : date.fromisoformat(x[0]))
	except ValueError:
		return "ValueError"

	price_dict = {date.fromisoformat(dt):price for dt,price in sorted_list}

	date_list = list(price_dict.keys())
	first_date = date_list[0]
	last_date = date_list[-1]

	days_diff = last_date - first_date

	def closest_date(last_date, iterator, no_of_days):
		date_range = [dt for dt in iterator if dt <= last_date - timedelta(days = no_of_days)]
		return max(date_range)

	if days_diff.days < 90:
		date_before_90 = None
	else:
		date_before_90 = closest_date(last_date, date_list, 90)

	if days_diff.days < 60:
		date_before_60 = None
	else:
		date_before_60 = closest_date(last_date, date_list, 60)
	
	if days_diff.days < 30:
		date_before_30 = None
	else:
		date_before_30 = closest_date(last_date, date_list, 30)

	if date_before_30 == None:
		price_before_30 = None
	else:
		price_before_30 = price_dict[last_date] - price_dict[date_before_30]

	if date_before_60 == None:
		price_before_60 = None
	else:
		price_before_60 =  price_dict[last_date] - price_dict[date_before_60]

	if date_before_90 == None:
		price_before_90 = None
	else:
		price_before_90 = price_dict[last_date] - price_dict[date_before_90]

	analysis = [price_before_30, price_before_60, price_before_90]
	return analysis