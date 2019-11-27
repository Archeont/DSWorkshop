hello = "Hello World!"
print(hello)
hello = 3
print(hello)


from our_module import  print_x_times


print_x_times(hello, 31)
##########################################

print(type(3))
print(type(3.14))
print(type(3 + 14j))
print(type(True))
print(type('Student'))
print(type(['Student', 'Błażej', 'Witek', 'Emil', 'Seba', 'Abażur', True]))
print(type(('Student', 'Błażej', 'Witek', 'Emil', 'Seba', 'Abażur', True)))
print(type({'Student', 'Błażej', 'Witek', 'Emil', 'Seba', 'Abażur', True}))
print(type({'Student': 'Błażej', 'Dziekan': 'Witek'}))

##########################################

import csv
import os
from time import time
from copy import copy


dir_path = os.path.dirname(__file__)
dir_path = os.path.dirname(dir_path)
file_path = os.path.join(dir_path, 'Static_data/bitcoin.csv')


beg = time()
with open(file_path, 'r') as f:
    reader = csv.reader(f)
    bitcoin_list = list(reader)

print(round(time() - beg, 2))
print(len(bitcoin_list))

##########################################

bitcoin_list_cpy = copy(bitcoin_list)
beg = time()
# for idx, row in enumerate(bitcoin_list):
#     if 'NaN' in row:
#         bitcoin_list.remove(row)

print("For loop", round(time() - beg, 2))
print(len(bitcoin_list))

##########################################

bitcoin_list = copy(bitcoin_list_cpy)
beg = time()
bitcoin_list = [row for row in bitcoin_list if 'NaN' not in row]
print("List comprehension", round(time() - beg, 2))
print(len(bitcoin_list))
