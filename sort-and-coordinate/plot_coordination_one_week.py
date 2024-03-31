import matplotlib.pyplot as plt
import pandas as pd

for i in range(1,13):
    df = pd.read_csv(f'weeks_csv_results/7_day_data_{i}.csv')
    order = range(len(df))

    plt.scatter(x=df['Longitude'], y=df['Latitude'], c=order, cmap='viridis')
    plt.colorbar(label='Order of RX Time')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.savefig(f'week_plots/figure_{i}.png')
    plt.show()


