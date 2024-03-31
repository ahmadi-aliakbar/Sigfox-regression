import pandas as pd

df = pd.read_csv("sigfox_dataset_rural (1) - Copy.csv")
df['RX Time'] = pd.to_datetime(df['RX Time'].str.strip("'"))
df_sorted = df.sort_values(by='RX Time')
df_sorted.to_csv('sorted_file.csv', index=False)