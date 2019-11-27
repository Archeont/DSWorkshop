import os

import pandas as pd
import numpy as np


dir_path = os.path.dirname(__file__)
dir_path = os.path.dirname(dir_path)
file_path = os.path.join(dir_path, 'Static_data/degrees-that-pay-back.csv')


my_data = pd.read_csv(file_path, delimiter=',')
my_data.dropna(inplace=True)

print(my_data)

my_data['Starting Median Salary'] = my_data['Starting Median Salary'].apply(lambda x: x[1:])

my_data['Starting Median Salary'] = my_data['Starting Median Salary'].apply(lambda x: x.replace(",", ""))

my_data['Starting Median Salary'] = my_data['Starting Median Salary'].astype(np.float64)

my_data.loc[my_data['Starting Median Salary'] > 30000, 'Undergraduate Major']
my_data.iloc[my_data['Starting Median Salary'].values.argmax(), 0]

columns = ['Mid-Career Median Salary', 'Mid-Career 10th Percentile Salary', 'Mid-Career 25th Percentile Salary',
           'Mid-Career 75th Percentile Salary', 'Mid-Career 90th Percentile Salary']

for col in columns:
    my_data[col] = my_data[col].apply(lambda x: x[1:])
    my_data[col] = my_data[col].apply(lambda x: x.replace(",", ""))
    my_data[col] = my_data[col].astype(np.float64)

