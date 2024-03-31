import pandas as pd
from datetime import datetime, timedelta


df = pd.read_csv('sorted_file.csv')
df['RX Time'] = pd.to_datetime(df['RX Time'])
start_date = df['RX Time'].min()
end_date = start_date + timedelta(days=1)

for i in range(1,81):
    filtered_dfs = []

    current_date = start_date
    while current_date < end_date:
        filtered_df = df[df['RX Time'].dt.date == current_date.date()]

        filtered_dfs.append(filtered_df)

        current_date += timedelta(days=1)

    result_df = pd.concat(filtered_dfs)

    result_df.to_csv(f'days_csv_results/day_data_{i}.csv', index=False)

    start_date = end_date
    end_date += timedelta(days=1)
