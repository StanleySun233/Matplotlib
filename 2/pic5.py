import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('bjwind.csv')
print(data.head())

plt.plot(data['year'], data['date'], label='Year')
plt.scatter(data['year'], data['date'], c='orange', marker='*')
plt.xlabel('Year')
plt.ylabel('Wind Day')
plt.grid('on')

for i in range(len(data['year'])):
    plt.annotate(data['date'][i], xy=(data['year'][i], data['date'][i]), xytext=(data['year'][i] + 0.001, data['date'][i] + 0.001))
plt.show()
