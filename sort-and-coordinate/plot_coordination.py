import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sorted_file.csv")
order = range(len(df))

plt.scatter(x=df['Longitude'], y=df['Latitude'], c=order, cmap='viridis')
plt.colorbar(label='Order of RX Time')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig(f'map_plot/map_plot.pdf')
