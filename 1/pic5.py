import pandas as pd
import matplotlib.pyplot as plt

data0 = pd.read_csv('data.csv')

col = list(set(data0['住址']))
raw = list(data0['住址'])
data = [raw.count(i) for i in col]
sel = []

for i in range(len(col)):
    data[i] = [data[i], col[i]]
data[0][1] = '未知'
data.sort()
data.reverse()
del data[0]

col = []
raw = []
for i in data:
    col.append(i[0])
    raw.append(i[1])
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.pie(col, labels=raw)
plt.title("舟山医院诊疗病例住址饼图")
plt.show()
