nested_dict = {
	'01/01/2018' : 
	{
		'stock_1' : 
		{
			'opening' : 1,
			'high' : 2,
			'low' : 3,
			'closing' : 4
		},
		'stock_2' : 
		{
			'opening' : 11,
			'high' : 12,
			'low' : 13,
			'closing' : 14
		},
		'stock_3' : 
		{
			'opening' : 31,
			'high' : 32,
			'low' : 33,
			'closing' : 34
		}
	},
	'02/01/2018' : 
	{
		'stock_1' : 
		{
			'opening' : 111,
			'high' : 112,
			'low' : 113,
			'closing' : 114
		},
		'stock_2' : 
		{
			'opening' : 211,
			'high' : 212,
			'low' : 213,
			'closing' : 214
		},
		'stock_3' : 
		{
			'opening' : 331,
			'high' : 332,
			'low' : 333,
			'closing' : 334
		}
	},
	'03/01/2018' : 
	{
		'stock_1' : 
		{
			'opening' : 1111,
			'high' : 1112,
			'low' : 1113,
			'closing' : 1114
		},
		'stock_2' : 
		{
			'opening' : 2211,
			'high' : 2212,
			'low' : 2213,
			'closing' : 2214
		},
		'stock_3' : 
		{
			'opening' : 3331,
			'high' : 3332,
			'low' : 3333,
			'closing' : 3334
		}
	}
}

# jan0118, jan0218, jan0318 = nested_dict.values()
for date, stock in nested_dict.items():
	for stk, price in stock.items():
		print(date,'\t',stk )
		for key, value in price.items():
			print(key, value)
# jan0118_stk1, jan0118_stk2, jan0118_stk3 = jan0118.values()

# jan0118_stk1_open, jan0118_stk1_high, jan0118_stk1_low, jan0118_stk1_close = jan0118_stk2.values()

# print(jan0118_stk1_close)