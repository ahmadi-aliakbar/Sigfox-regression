import matplotlib.pyplot as plt
import pandas as pd


for i in range(1, 81):
    df = pd.read_csv(f'days_csv_results/day_data_{i}.csv')
    plt.figure()
    order = range(len(df))
    plt.scatter(x=df['Longitude'], y=df['Latitude'], c=order, cmap='viridis')
    plt.colorbar(label='Order of RX Time')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    plt.savefig(f'day_plots/figure_{i}.png')
    plt.close()
