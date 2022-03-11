import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import ticker

data = pd.read_csv('beijing.csv')
print(data.head())

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.set_xlabel('Year', fontdict={'size': 16})
ax1.plot(data['year'], data['nianjiangshui'], color='darkorange', linestyle='-', label='Rain Per Year')
ax1.set_ylabel('Rain Per Year', color='darkorange', fontdict={'size': 16})
ax1.scatter(data['year'], data['nianjiangshui'], marker='*', c='red')

ax2.plot(data['year'], data['fugailv'], color='olive', linestyle='--', label='SaiHanBa Forest Cover')
ax2.set_ylabel('SaiHanBa Forest Cover', color='olive', fontdict={'size': 16})
ax2.scatter(data['year'], data['fugailv'], marker='*', c='blue')

r1 = data['year'] - 0.125 - 0.025
barWidth = 0.25
r2 = [x + barWidth + 0.05 for x in r1]

ax3 = ax1.twinx()
ax3.bar(r1, data['nianjunAQI'], color='orange', alpha=0.3, label='AQI Per Year', width=barWidth)
ax3.axis('off')

for a, b in zip(r1, data['nianjunAQI']):
    plt.text(a - 0.25, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=16)

ax4 = ax1.twinx()
ax4.bar(r2, data['CO2xishou(wt)'], color='royalblue', alpha=0.3, label='CO2 Output', width=barWidth)
ax4.axis('off')

for a, b in zip(r2, data['CO2xishou(wt)']):
    plt.text(a + 0.25, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=16)

plt.grid('on')
plt.title('Comparative Analysis of SaihanBa And Beijing', fontdict={'size': 20})
lines = []
labels = []

for ax in fig.axes:
    axLine, axLabel = ax.get_legend_handles_labels()
    lines.extend(axLine)
    labels.extend(axLabel)

ax1.legend(lines, labels,
           loc='upper left')

plt.show()
