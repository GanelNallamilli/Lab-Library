
import numpy as np
import lab
import matplotlib.pyplot as plt
import random

def test_scatter_graph():
    '''Generates Sample Data'''
    max = 100
    divide = 10
    xData = [i for i in range(int(max/divide))]
    yData = [random.randint(i-divide,i) for i in range(0,max,divide)]
    xError = [random.randint(0,1) for i in range(int(max/divide))]
    yError = [random.randint(5,10) for i in range(int(max/divide))]

    #Tests the scattergraph module in lab module
    ax = lab.scattergraph(xData,yData, yError = yError,xError = 0,error_label = "Error Uncertainty", data_label = "Data")
    plt.show()


#Run testing functions here.
if __name__ == '__main__':
    test_scatter_graph()
