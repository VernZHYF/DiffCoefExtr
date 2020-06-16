from averPlotRet import *
from lineFitting import *
from normFit import *

# fixed parameter
Dd = 0.01
timeSteps = 80
numCases = 16

path = sys.argv[1]

dataSets = dataExtr(path, timeSteps, numCases)
stdList = []
x = np.linspace(0, timeSteps, timeSteps)
for i in range(timeSteps):
    averageData = averPlotRet(dataSets[i], 0, numCases)
    mean, std, amplitude = normFit(averageData)
    stdList.append(std ** 2)

fig4 = plt.figure(3)
plt.plot(x, stdList)
plt.title("stdSquare - t")
plt.xlabel("t")
plt.ylabel("Square of STD")


D = lineFitting(x, stdList)

with open("result.txt", "w") as f:
    f.write("D = {}".format(D))

plt.savefig("FittingCurve")
