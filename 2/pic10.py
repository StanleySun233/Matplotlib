import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from matplotlib import pyplot as plt


def stdError_func(y_test, y):
    return np.sqrt(np.mean((y_test - y) ** 2))


def R2_1_func(y_test, y):
    return 1 - ((y_test - y) ** 2).sum() / ((y.mean() - y) ** 2).sum()


def R2_2_func(y_test, y):
    y_mean = np.array(y)
    y_mean[:] = y.mean()
    return 1 - stdError_func(y_test, y) / stdError_func(y_mean, y)


def maxminnorm(array):
    sum = 0
    for i in array:
        for j in i:
            sum += j
    a = []
    p = 0
    for i in array:
        a.append([])
        for j in i:
            a[p].append(j)
    p += 1
    return np.array(a)


filename = "price.csv"
df = pd.read_csv(filename)
x = np.array(maxminnorm(df.iloc[:, 1:5].values))

y = np.array(maxminnorm(df.iloc[:, 6].values))

cft = linear_model.LinearRegression()
print(x.shape)
cft.fit(x, y)  #

print("model coefficients", cft.coef_)
print("model intercept", cft.intercept_)

predict_y = cft.predict(x)
strError = stdError_func(predict_y, y)
R2_1 = R2_1_func(predict_y, y)
R2_2 = R2_2_func(predict_y, y)
score = cft.score(x, y)

print('strError={:.2f}, R2_1={:.2f},  R2_2={:.2f}, clf.score={:.2f}'.format(strError, R2_1, R2_2, score))

plt.plot(df['Forest Cover'], np.array(df.iloc[:, 1:5].values))
plt.grid('on')
plt.show()

coef = [-97671.6522898, 1841.4218808, 69831.93958451]
