import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data2.csv')
print(data.head())

ds = data['S']
dS = data['SUM']
year = data['year']

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(year, ds*100, color='blue', linestyle='-', label='S')
ax1.scatter(year, ds*100, c='green')
ax1.set_xlabel('Year', fontdict={'size': 16})
ax1.set_ylabel('S', fontdict={'size': 16})

ax2.plot(year, dS, color='red', linestyle='--', label='Price')
ax2.set_ylabel('Price', fontdict={'size': 16})
ax2.scatter(year, dS, c='gray')

lines = []
labels = []
for ax in fig.axes:
    axLine, axLabel = ax.get_legend_handles_labels()
    lines.extend(axLine)
    labels.extend(axLabel)

ax1.legend(lines, labels,
           loc='upper left')
plt.show()
