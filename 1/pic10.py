import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data0 = pd.read_csv('../dataSheet/data.csv')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

sns.heatmap(data=data0.corr(), linecolor="white", annot=True, linewidths=0.1)

plt.show()
