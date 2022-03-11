import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data0 = pd.read_csv('../dataSheet/data.csv')

col = list(set(data0['身份']))
raw = list(data0['身份'])
data = [raw.count(i) for i in col]
sel = []

for i in range(len(col)):
    data[i] = [data[i], col[i]]
data.sort()
data.reverse()

col = []
raw = []
for i in data:
    col.append(i[0])
    raw.append(i[1])

plt.pie(col,labels=raw)
plt.title("舟山医院诊疗病例身份饼图")
plt.show()
