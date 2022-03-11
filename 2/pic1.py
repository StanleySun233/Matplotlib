import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import ticker

data = pd.read_csv('data.csv')
print(data.head())


def Rate(_data):
    temp = []
    cnt0 = float(_data[0])
    for i in _data:
        cnt1 = float(i)
        temp.append((cnt1 - cnt0) / cnt1)
        cnt0 = cnt1
    del temp[0]
    temp1 = pd.DataFrame(data=temp, columns=['Rate'], index=None)
    return temp1


rate1 = Rate(data['Tree Volume'])
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.set_xlabel('Year', fontdict={'size': 16})
ax1.plot(data['Year'], data['Tree Volume'], color='darkorange', linestyle='-', label='Cover Area')
ax1.set_ylabel('Tree Volume', color='darkorange', fontdict={'size': 16})

ax2.plot(data['Year'][0:59], rate1, color='olive', linestyle='--', label='Rate')
ax2.set_ylabel('Rate Growth', color='olive', fontdict={'size': 16})
ax2.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))

plt.grid('on')
plt.title('Tree Volume in SaiHanBa', fontdict={'size': 20})
plt.show()
