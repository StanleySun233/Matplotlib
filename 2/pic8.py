import pandas as pd
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from scipy.optimize import leastsq
#
x1 = [85.74, 230.43, 2458, 3687]
x2 = [631.04, 892.17, 17248.67, 25873]
x3 = [3392.48, 4770.06, 101761.33, 152642]
x4 = [97.34, 133.08, 2838.67, 4258]
Y = [4206.6, 6025.73, 124306.67, 186460]
year = [1962, 1982, 2002, 2021]

data = pd.read_csv('data.csv')
x1 = data['Forest Cover']
x3 = data['CO2 Saved']
#
# plt.figure(1)
# plt.subplots(1, 2)
# plt.subplot(121)
# plt.scatter(year, x1, c='red', s=100, label='Forest Soil')
# plt.scatter(year, x3, c='green', s=100, label='Forest Carbon')
#
# for i in range(len(year)):
#     plt.annotate(x1[i], xy=(year[i], x1[i] * 1.2), xytext=(year[i] + 0.5, x1[i] * 1.1))
#     plt.annotate(x2[i], xy=(year[i], x3[i] * 0.8), xytext=(year[i] + 0.5, x3[i] * 0.9))
#
# plt.legend()
#
# plt.subplot(122)
# plt.scatter(year, x2, c='blue', marker='2', s=300, label='Biodiversity Index')
# plt.scatter(year, x4, c='black', marker='2', s=300, label='Others')
# plt.legend()
# plt.show()
#
# plt.figure(2)
# plt.scatter(year, Y, c='yellow', marker='*', s=300, label='SUM')
# plt.legend('1')
# plt.show()
#
# plt.figure(3)

# hypothesis function

def hypothesis_func(w, train_x):
    w2, w1, w0 = w
    return w2 * train_x * train_x + w1 * train_x + w0


# error function误差函数
def error_func(w, train_x, train_y):
    error = hypothesis_func(w, train_x) - train_y
    return error


def dump_fit_func(w_fit):
    w2, w1, w0 = w_fit
    print("fitting line=" + str(w2) + "*x^2 + " + str(w1) + "*x + " + str(w0))
    return


# square error平方差函数
def dump_fit_cost(w_fit, train_x, train_y):
    error = error_func(w_fit, train_x, train_y)
    square_error = sum(e * e for e in error)
    print('fitting cost:', str(square_error))
    return square_error


if __name__ == '__main__':
    # train set
    train_x1 = np.array(x1)
    train_x2 = np.array(x3)

    # linear regression by leastsq
    w_init = [1, 1, 1]  # weight factor init
    fit_ret = leastsq(error_func, w_init, args=(train_x1, train_x2))
    w_fit = fit_ret[0]

    # dump fit result
    dump_fit_func(w_fit)
    fit_cost = dump_fit_cost(w_fit, train_x1, train_x2)

    # test set
    test_x = np.linspace(train_x1.min(), train_x1.max(), 10)
    test_y = hypothesis_func(w_fit, test_x)

    # show result by figure
    plt.figure(figsize=(10, 10))
    plt.scatter(train_x1, train_x2, c='k', label="train set")
    plt.scatter(test_x, test_y, c='r', marker='^', label='test set', linewidth=2)
    plt.plot(test_x, test_y, c='r', label="fitting line")
    plt.legend(loc='lower right')  # 绘制图例
    plt.show()

