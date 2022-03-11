import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data0 = pd.read_csv('../dataSheet/data.csv')

begTime = data0['入院日期'] / 1000 / 3600
endTime = data0['出院日期'] / 1000 / 3600
date = endTime - begTime
plt.scatter(range(len(begTime)), date, c='green', marker='*', alpha=0.4, label="费用点")
plt.title("舟山医院诊疗病例住院时间图")
plt.show()