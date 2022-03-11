import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data0 = pd.read_csv('../dataSheet/data.csv')

price = data0['总费用']
s = sum(price)
average = [s / len(price)] * len(price)

plt.plot(range(len(price)), average, label='平均费用线', color='green')
plt.legend()
plt.title("舟山医院诊疗病例费用散点图")
plt.show()