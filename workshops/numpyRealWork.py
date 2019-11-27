import os
import numpy as np
import pandas as pd
from time import time, strftime, localtime
import warnings
warnings.filterwarnings("error")


dir_path = os.path.dirname(__file__)
dir_path = os.path.dirname(dir_path)
file_path = os.path.join(dir_path, 'Static_data/bitcoin.csv')

beg = time()
my_data = pd.read_csv(file_path, delimiter=',')
my_data.dropna(inplace=True)
print(time() - beg)

close_price = my_data["Close"].values
timestamp = my_data["Timestamp"].values

close_price_moved = np.copy(close_price)
close_price_moved = np.insert(close_price_moved, 0, 0)
close_price_moved = close_price_moved[:-1]

close_price_difference = close_price - close_price_moved
close_price_bools = close_price_difference >= 0
prev_price_bool = True
auctions = 1
money = 0

for idx, price_bool in enumerate(close_price_bools):
    if prev_price_bool != price_bool:
        if price_bool:
            auctions = money/close_price[idx - 1]
            money = 0
        else:
            try:
                money = auctions*close_price[idx - 1]
            except RuntimeWarning:
                print(strftime('%Y-%m-%d', localtime(timestamp[idx])))
                break
            auctions = 0
    # print("money: ", money, " auctions: ", auctions, " close: ", close_price[idx])
    prev_price_bool = price_bool


print("mamona", money + auctions*close_price[-1])

auctions = 100
money = 0


print(close_price[-1])
print("mamona", money + auctions*close_price[-1])
