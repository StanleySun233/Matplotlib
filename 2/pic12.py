import pandas as pd
from matplotlib import pyplot as plt

d1 = pd.read_csv('julei.csv')
d2 = pd.read_csv('julei2.csv')
d3 = pd.read_csv('julei3.csv')

plt.scatter(d3['Lat'], d3['Lon'])
plt.xlabel('Lat')
plt.ylabel('Lon')
for i in range(len(d3['Lat'])):
    plt.annotate(str(d3['AQI'][i]), xy=(d3['Lat'][i], d3['Lon'][i]), xytext=(d3['Lat'][i] + 0.001, d3['Lon'][i] + 0.001))

plt.show()
