import os
import pandas as pd
from sys import argv

script, folder, data_file = argv 
base_folder = os.chdir(folder)
df = pd.read_csv(data_file)

new_data = pd.DataFrame(columns = ['name', 'code', 'amt', 'date'])

sorted_file = sorted(os.listdir(base_folder), key = lambda x : int(x.split('-')[0]))

for file in sorted_file:
	data = pd.read_excel(file)
	data = data.rename(columns = {'Names' : 'name', 'A/c no' : 'code', 'Amount' : 'amt', 
                                          'Payment Date' : 'date'})
	data = data.drop(columns = ['Sl. No', 'Debit Account', 'IFSC Code',
                                        'Narration1', 'Narration2', 'email id'])
	new_data = pd.concat([new_data, data], sort = False, ignore_index = True)


df = pd.concat([df, new_data], sort = False, ignore_index = True)

df.to_csv(data_file, index = False)
print(f"Total Salary : {new_data['amt'].sum()}")