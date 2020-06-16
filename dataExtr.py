import pandas as pd
import os
import numpy as np


# def dataExtr():
#     dataSets = np.zeros((40, 400), dtype=np.float64)
#     i = 0
#     for fileName in os.listdir("data"):
#         data = pd.read_csv("data/" + fileName + "/C7900.res", header=None)
#         dataSets[i, :] = data[0].tolist()
#         i = i + 1
#     return dataSets

# 80 - 80个时间步，40 - 40个暂定平均样本空间，400 - 竖向的总的网格数
def dataExtr(path, timeSteps, numCases):
    dataSets = np.zeros((80, 40, 400), dtype=np.float64)
    # i - 时间戳， j - 样本序列
    i = 0
    j = 0
    seq = 0
    for fileName in os.listdir(path):
        while seq < 100*timeSteps:
            # print("data/" + fileName + "/C" + str(seq) + ".res")
            data = pd.read_csv(path+"/" + fileName + "/C" + str(seq) + ".res", header=None)
            data = data[0].tolist()
            dataSets[i, j, :] = data
            i = i + 1
            seq = seq + 100
        i = 0
        seq = 0
        j = j + 1

    return dataSets
