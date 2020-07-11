import quorachallenge
from datetime import date,timedelta


class Stockinfo:


    # @quorachallenge.autotest('stock_analysis')
    @quorachallenge.autotest('advanced_stock')
    def stock(self,prices):
    	try:
    		sorted_list = sorted(prices,key = lambda x : date.fromisoformat(x[0]))
    		sorted_list = list(map(lambda x: (date.fromisoformat(x[0]), x[1]), sorted_list))
    	except ValueError:
    		return "ValueError"

    	price_dict = {dt:price for dt,price in sorted_list}

    	date_list = list(price_dict.keys())
    	first_date = date_list[0]
    	last_date = date_list[-1]

    	days_diff = last_date - first_date

    	def closest_date(self,last_date, iterator, no_of_days):
    		date_range = [dt for dt in iterator if dt <= last_date - timedelta(days = no_of_days)]
    		return max(date_range)


    	date_before_list = [None if days_diff.days < i
    							else closest_date(last_date,date_list,i)
    							for i in range(30,91,30)]

    	price_list = [None if i == None else price_dict[last_date] - price_dict[i] for i in date_before_list]

	# return price_list    # uncomment this for @quorachallenge.autotest('stock_analysis')

    	def percentage_change(last_date,date_before_list, sorted_list, price_dict):
    		all_date_list = [pair[0] for pair in sorted_list]
    		all_price_list = [pair[1] for pair in sorted_list]
    		result = []
    		for dt in date_before_list:
    			if dt is None:
    				result.append((None, None))
    			else:
    				start = all_date_list.index(dt)
    				end = all_date_list.index(last_date)
    				growth = 0
    				search_price_list = all_price_list[start : end +1]
    				for index, _ in enumerate(search_price_list):
    					if index == 0:
    						continue
    					else:
    						if search_price_list[index] > search_price_list[index-1]:
    							growth += 1
    				percent = round(((price_dict[last_date] - price_dict[dt])/ price_dict[dt])*100, 1)
    				result.append((percent, growth))

    		return tuple(result)

    	return percentage_change(last_date, date_before_list, sorted_list, price_dict)

