from numpy.linalg import inv  # 矩阵求逆
from numpy import dot  # 求矩阵点乘
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data.csv')
dataset = pd.DataFrame(data, copy=True)
test = dataset.iloc[:, 0:7]
test = test.copy()
X = test.iloc[:, [1, 2, 3, 4, 5, 6]]
Y = test.iloc[:, 0]
print(X)
print(Y)
theta = dot(dot(inv(dot(X.T, X)), X.T), Y)
y = dot(theta, X.T)
print('权重', theta)  # 权重
loss = np.array(Y - y)  # 残差
print('残差', loss)

