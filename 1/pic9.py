import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data0 = pd.read_csv('../dataSheet/data.csv')

price = data0['总费用']
name = data0['诊断名称']

plt.hist(data0['年龄'], bins=20)
plt.title('舟山医院看病年龄直方图')
plt.xlabel('年龄')
plt.ylabel('数量')
plt.grid('on')
plt.show()