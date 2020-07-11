import pandas as pd
from sys import argv

script, filename, filename2 = argv

df = pd.read_csv(filename)

df2 = pd.read_csv(filename2)

start = df.loc[pd.isnull(df['month']) == True].head(1).index[0]

total_sal_month = {m : a for (m, a) in zip(df2['month'], df2['amt'])}

if not len(df['month']) == df['month'].isna().sum():
	current_sal = {m : df.loc[df['month'] == m, 'amt'].sum() for m in df2['month']}
else:
	current_sal = {m : 0 for m in df2['month']}

current_status = [True if current_sal[key] > total_sal_month[key] 
                  else False 
                  for key in total_sal_month.keys()]

index_value = [(i, m) for (i, m) in zip(df2.index, df2['month'])]
index_value_2 = [(m, i) for (i, m) in zip(df2.index, df2['month'])]

index_value.extend(index_value_2)

index_dict = {a : b for a,b in index_value}

for a in df[start:].itertuples():
	index = a[0]
	rdf = df.loc[ :index]
	last_found_month = rdf.loc[rdf['code'] == df.loc[index, 'code'], 'month'].tail(2).head(1)
	current_index_sal = df.at[index, 'amt']
	if index == 0:
		df.at[index, 'month'] = str
		df.at[index, 'month'] = index_dict[current_status.index(False)]
		current_sal[df.at[index, 'month']] += current_index_sal
	else:
		if pd.isnull(df.at[index, 'month']):
			if not pd.isnull(last_found_month.iloc[0]):
				last_found_month = last_found_month.iloc[0]
				check_from_month_index = index_dict[index_dict[index_dict[last_found_month] + 1]]
				current_index_month = index_dict[current_status[check_from_month_index : ].index(False) + check_from_month_index]
				df.at[index, 'month'] = current_index_month
				current_sal[df.at[index, 'month']] += current_index_sal
				if current_sal[current_index_month] > total_sal_month[current_index_month]:
					current_status[index_dict[current_index_month]] = True
			else:
				current_index_month = index_dict[current_status.index(False)]
				df.at[index, 'month'] = current_index_month
				current_sal[df.at[index, 'month']] += current_index_sal
				if current_sal[current_index_month] > total_sal_month[current_index_month]:
					current_status[index_dict[current_index_month]] = True
       
df2['current_salary'] = current_sal.values()

df.to_csv(filename, index = False)
df2.to_csv(filename2, index = False)