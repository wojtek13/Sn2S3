#########################################################################
####################### IMPORTING REQUIRED MODULES ######################

import numpy as np
import pylab
from scipy.optimize import leastsq  # Levenberg-Marquadt Algorithm #




#########################################################################
########################### DEFINING FUNCTIONS ##########################

def lorentzian(x, coefficients):
    y = 0
    if len(coefficients)==8:
        # within_bounds = (coefficients[0][1]>515)*(coefficients[1][1]<490)*(515>coefficients[2][1]>480) * \
        within_bounds =(coefficients[0][2]>0)*(coefficients[1][2]>0)*(coefficients[2][2]>0)*(coefficients[3][2]>0)*\
                       (coefficients[4][2]>0)*(coefficients[5][2]>0)*(coefficients[6][2]>0)*(coefficients[7][2]>0)*\
                       (315<coefficients[5][1]<320)*(193<coefficients[7][1]<197)
    elif len(coefficients)==3:
        within_bounds =(coefficients[2][2]>0)*(coefficients[1][2]>0)*(465<coefficients[2][1]<485)*(499>coefficients[1][1]>493)
    else:
        within_bounds=True
    for p in coefficients:
        numerator = (p[0] ** 2)
        denominator = (x - (p[1])) ** 2 + p[0] ** 2
        y += p[2] * (numerator / denominator)
    y+=coefficients[0][3]
    if within_bounds:
        return y
    else:
        return -10e10


def residuals(p, y, x):
    elements_number = len(p)
    coefficients = []
    if elements_number % 4 == 0:
        for i in range(0, elements_number / 4):
            coefficients.append(p[4 * i: 4 * (i + 1)])
    else:
        raise Exception('Number of coefficients provided for residuals(p,y,x) is wrong!!!')
    err = y - lorentzian(x, coefficients)

    return err


def perform_fitting(X, Y):
    peak185_range=(X>181)*(X<189)
    peak210_range=(X>206)*(X<214)
    peak240_range=(X>236)*(X<244)
    peak254_range=(X>250)*(X<258)
    peak310_range=(X>300)*(X<320)
    peak156_range=(X>152)*(X<160)
    peak193_range=(X>193)*(X<197)
    coefficients = [[7, 185, max(Y[peak185_range])-100, 100],[5, 210, max(Y[peak210_range])-100, 0], [14, 240, max(Y[peak240_range])-100, 0],
                    [15, 254, max(Y[peak254_range])-100, 0], [7, 310, max(Y[peak310_range])-100, 0], [5, 317, 0.5*max(Y[peak310_range])-30, 0],
                    [5, 155.5, max(Y[peak156_range]), 0], [3, 195, max(Y[peak193_range])-100, 0]]
    # print (coefficients)
    fitting_range=(X>150)*(X<330)
    pbest = leastsq(residuals, coefficients, args=(Y[fitting_range], X[fitting_range]), full_output=1)
    best_parameters = []
    #print pbest[0]
    for i in range(0, int(len(pbest[0])/4)):
        best_parameters.append(pbest[0][4*i : 4*(i+1)])

    #names = ["185", "210", "240", "254", "310", "324", "156", "193"]
    #for i in range(len(best_parameters)):
    #    pylab.plot(X[fitting_range],  lorentzian(X[fitting_range], [best_parameters[i]]), label=names[i])
    #pylab.plot(X[fitting_range], Y[fitting_range], 'o', label="data")
    #pylab.plot(X[fitting_range], lorentzian(X[fitting_range], best_parameters), '-', label="fit")
    #pylab.legend()
    #pylab.show()

    return best_parameters


#########################################################################
def main():
    Data = np.loadtxt("2015-09-14_Sn2S3_MonikaWojtek/090_VH_Sn2S3.txt")
    X=Data[:,0]
    Y=Data[:,1]
    fitting_range=(X>150)*(X<330)
    fitParameters = perform_fitting(X, Y)
    names = ["185", "210", "240", "254", "310", "324", "156", "193"]
    for i in range(len(fitParameters)):
        pylab.plot(X[fitting_range],  lorentzian(X[fitting_range], [fitParameters[i]]), label=names[i])
    pylab.plot(X[fitting_range], Y[fitting_range], 'o', label="data")
    pylab.plot(X[fitting_range], lorentzian(X[fitting_range], fitParameters), '-', label="fit")
    pylab.legend(loc = 2)
    pylab.show()

#########################################################################
if __name__ == "__main__":
    main()