import matplotlib.pyplot as plt
import numpy as np


# dataSets - 整个数据集的样本索引号-domainSize切片
# begin - 样本索引号起点   end - 样本索引号终点
# Functions: 返回样本索引号起点到样本索引号终点范围内，所有数据算数加和的平均值曲线,
#            并返回最终的计算平均值

def averPlotRet(dataSets, begin, end):
    temp = np.zeros((1, 400), dtype=np.float64)

    # fig = plt.figure(0)
    # plt.title("Vertical Scalar Spreading")
    # plt.ylabel("Dimensionless Concentration Number")
    # plt.xlabel("X")

    for i in range(begin, end):
        temp = temp + dataSets[i, :]
        # plt.plot(dataSets[i, :])

    temp = temp / (end - begin)

    fig2 = plt.figure(1)
    plt.title("Average Scalar Spreading of {} cases".format(end - begin))
    plt.ylabel("Dimensionless Concentration Number")
    plt.xlabel("X")
    plt.ylim(-1, 35)
    plt.plot(temp[0, :])

    return temp[0, :]
