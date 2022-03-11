import pandas as pd
import matplotlib.pyplot as plt

data0 = pd.read_csv('../dataSheet/data.csv')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

price = data0['总费用']
name = data0['诊断名称']

col = []

for i in range(len(price)):
    col.append([price[i], name[i]])

col.sort(reverse=True)
col = col[:10]

data = []
index = []
for i in col:
    data.append(i[0])
    index.append(i[1])

plt.bar(index, data)
plt.plot(index, data, color='red')

for i in range(len(data)):
    plt.annotate(str(data[i]), xy=(i, data[i]), xytext=(i-0.25, data[i]+100))

plt.title("舟山医院诊疗病例报价前十统计")
plt.show()
