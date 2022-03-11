import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data2.csv')
print(data.head())

da = data['D+']
dm = data['D-']
ds = data['S']
year = data['year']
rk = data['rank']

plt.scatter(da, dm, alpha=1, marker='2', s=250, c='m', label='Year')
plt.scatter(da, dm, alpha=1, marker='*', s=50, c='r')
plt.xlabel("D+")
plt.ylabel("D-")
for i in range(len(year)):
    if i <= 0:
        plt.annotate(str(year[i]) + ", S = " + str(int(ds[i] * 10000) / 10000) + ", rank = " + str(rk[i]),
                     xy=(da[i], dm[i]), xytext=(da[i] + 0.001, dm[i] + 0.001))
    elif 2 < i <= 15:
        continue
    elif i % 5 == 0:
        plt.annotate(str(year[i]) + ", S = " + str(int(ds[i] * 10000) / 10000) + ", rank = " + str(rk[i]),
                     xy=(da[i], dm[i]), xytext=(da[i] + 0.001, dm[i] + 0.001))
    elif i > len(year) - 6:
        plt.annotate(str(year[i]) + ", S = " + str(int(ds[i] * 10000) / 10000) + ", rank = " + str(rk[i]),
                     xy=(da[i], dm[i]), xytext=(da[i] + 0.001, dm[i] + 0.001))
plt.legend()
plt.show()
