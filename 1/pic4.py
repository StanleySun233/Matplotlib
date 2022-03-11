import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data0 = pd.read_csv('../dataSheet/data.csv')
data0.dropna(subset=['年龄'], inplace=True)

m = []
fm = []

for i in range(len(data0['性别'])):
    try:
        if data0['性别'][i] == '男':
            m.append(data0['年龄'][i])
        else:
            fm.append(data0['年龄'][i])
    except:
        print("数据有误，出错在{}行，默认删除".format(i))
        continue
data = [m, fm]
plt.boxplot(x=data,  # 指定绘图数据
            labels=['男', '女'],  # 性别
            patch_artist=True,  # 要求用自定义颜色填充盒形图，默认白色填充
            showmeans=True,  # 以点的形式显示均值
            boxprops={'color': 'black', 'facecolor': '#9999ff'},  # 设置箱体属性，填充色和边框色
            flierprops={'marker': 'o', 'markerfacecolor': 'red', 'color': 'black'},  # 设置异常值属性，点的形状、填充色和边框色
            meanprops={'marker': 'D', 'markerfacecolor': 'indianred'},  # 设置均值点的属性，点的形状、填充色
            medianprops={'linestyle': '--', 'color': 'orange'})  # 设置中位数线的属性，线的类型和颜色
plt.tick_params(top='off', right='off')
plt.ylabel("年龄分布")
plt.title("舟山医院年龄分布箱型图")
plt.show()
