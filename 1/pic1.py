import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data0 = pd.read_csv('../dataSheet/data.csv')

order = ['95-99', '90-94', '85-89', '80-84',
         '70-74', '75-79', '65-69', '60-64', '55-59',
         '50-54', '45-49', '40-44', '35-39', '30-34',
         '25-29', '20-24', '15-19', '10-14', '5-9', '0-4']

orderr = order[::-1]

m = [0 for i in range(len(order))]
fm = [0 for i in range(len(order))]
temp = []

for i in range(len(data0['年龄'])):
    if str(data0['年龄'][i]) == 'nan':
        continue
    ag = (int(data0['年龄'][i]) // 5)
    if data0['性别'][i] == '男':
        m[ag] += 1
    else:
        fm[ag] += 1

ms = sum(m)
fms = sum(fm)

for i in range(len(m)):
    m[i] = int((m[i] / ms) * 100)

for i in range(len(fm)):
    fm[i] = int(-(fm[i] / fms) * 100)

data = {
    'm': m,
    'fm': fm,
    'index': orderr
}
Pyramid_Data = pd.DataFrame(data)

bar_plot = sns.barplot(y='index', x="m", color="red", data=Pyramid_Data, order=order)
bar_plot = sns.barplot(y='index', x="fm", color="blue", data=Pyramid_Data, order=order)
plt.xticks([-4, -2, 0, 2, 4], [4, 2, 0, 2, 4, ])

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
bar_plot.set(xlabel="看病年龄占比（%）", ylabel="年龄层", title="舟山医院看病年龄占比金字塔")
plt.show()

