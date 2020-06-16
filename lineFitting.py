from scipy import optimize
import matplotlib.pyplot as plt


def func(x, A, B):
    return A * x + B


def lineFitting(x, stdList):
    size = int(len(x)/2)

    A, B = optimize.curve_fit(func, x[size:], stdList[size:])[0]
    y1 = A * x + B

    plt.plot(x, y1, "red")

    return A
