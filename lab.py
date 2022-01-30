import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import scipy.optimize

def scattergraph(xData,yData, xError = 0, yError = 0,error_label = "",error_alpha = 1,error_color = "blue", data_color = "black", marker_icon = "x",data_label = ""):
    fig, ax = plt.subplots()

    xData = np.array(xData)
    yData = np.array(yData)
    xError = np.array(xError)
    yError = np.array(yError)

    upperFit = yData+yError
    lowerFit = yData-yError
    ax.fill_betweenx(yData, xData-xError, xData+xError,alpha = error_alpha,color = error_color)
    ax.fill_between(xData, lowerFit, upperFit,alpha = error_alpha,color = error_color,label = error_label)
    ax.scatter(xData,yData,marker = marker_icon,color = data_color,label = data_label)
    plt.rcdefaults()
    plt.rcParams.update({
        "figure.facecolor":  ('#e0e0e0'),  # red   with alpha = 30%
        "axes.facecolor":    ('#f0f0ff'),  # green with alpha = 50%
        "savefig.facecolor": (0.0, 0.0, 1.0, 0.2),  # blue  with alpha = 20%
    })
    plt.legend(loc = "upper right")
    return ax