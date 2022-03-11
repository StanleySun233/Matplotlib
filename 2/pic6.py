import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
data = pd.read_csv('bjhaz.csv')
print(data.head())


def randrange(n, vmin, vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100
for c, m, zlow, zhigh in [('r', '*', -50, -25), ('b', '^', -30, -5)]:
    xs = data['1']
    ys = data['2']
    zs = data['3']
    ax.scatter(xs, ys, zs, c=c, marker=m)
ax.set_xlabel('Sand Blowing')
ax.set_ylabel('Floating Dust')
ax.set_zlabel('Sandstorm')
for i in range(len(data['year'])):
    ax.text(data['1'][i],data['2'][i],data['3'][i],data['year'][i])
plt.show()