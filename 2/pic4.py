import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.collections import LineCollection

n = 10
x = np.arange(0, n, step=.5)
y = x ** 2
norm = plt.Normalize(y.min(), y.max())
norm_y = norm(y)
map_vir = cm.get_cmap(name='viridis')
color = map_vir(norm_y)

data = pd.read_csv('beijing.csv')
print(data)

plt.bar(data['year'], data['nianjiangshui'], color=color)
for a, b in zip(data['year'], data['nianjiangshui']):
    plt.text(a, b + 0.5, '%.0f' % b, ha='center', va='bottom', fontsize=16)

plt.xlabel('Year', fontdict={'size': 20}, color='green')
plt.ylabel('Annual Precipitation', fontdict={'size': 20}, color='blue')
plt.show()
