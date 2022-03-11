import random as rd

import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('bjhaz.csv')
print(data.head())

plt.scatter(data['2'], data['3'])

t = []
for i in range(len(data['year'])):
    if [data['2'][i], data['3'][i]] not in t:
        plt.annotate(data['year'][i], xy=(data['2'][i], data['3'][i]), xytext=(data['2'][i], data['3'][i]))
        t.append([data['2'][i], data['3'][i]])
plt.show()
