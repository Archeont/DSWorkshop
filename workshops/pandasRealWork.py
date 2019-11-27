import os
import time

import pandas as pd
import matplotlib.pyplot as plt


dir_path = os.path.dirname(__file__)
dir_path = os.path.dirname(dir_path)
file_path = os.path.join(dir_path, 'Static_data/bitcoin.csv')


my_data = pd.read_csv(file_path, delimiter=',')
my_data.dropna(inplace=True)

my_data['Timestamp'] = my_data['Timestamp'].apply(lambda x: time.strftime('%Y-%m-%d', time.localtime(x)))
my_data_grouped = my_data.groupby('Timestamp')
close_prices_max_day = my_data_grouped['Close'].max()

close_prices = close_prices_max_day[-100:]

m12 = close_prices.ewm(span=12, adjust=False).mean()
m26 = close_prices.ewm(span=26, adjust=False).mean()
macd = m12 - m26
signal = macd.ewm(span=9, adjust=False).mean()

plt.plot(macd, label="MACD")
plt.plot(signal, label="Signal")
plt.legend(loc='upper left')

plt.show()
