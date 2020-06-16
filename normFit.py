from astropy import modeling
from dataExtr import *
import matplotlib.pyplot as plt

def normFit(dataSet):
    x = np.linspace(-200, 200, 400)

    fitter = modeling.fitting.LevMarLSQFitter()
    model = modeling.models.Gaussian1D()
    fitted_model = fitter(model, x, dataSet)

    # fig3 = plt.figure(2)
    # plt.plot(x + 200, dataSet)
    # plt.plot(x + 200, fitted_model(x))
    # plt.title("Data vs Fitted ", )
    # plt.ylabel("Dimensionless Concentration Number", )
    # plt.xlabel("X")

    return fitted_model.mean[0], fitted_model.stddev[0], fitted_model.amplitude[0]
