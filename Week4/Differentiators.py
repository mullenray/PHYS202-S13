import numpy as np

def fourPtFiniteDiff(x,y):
    """Input arrays x and y(x).
       Computes the numerical derrivative of y with respect to x using the four-point centre differencing method."""
    dydx = np.zeros(y.shape,float)
    for i,n in enumerate(y[2:-2]):
        i += 2
        dydx[i] = (y[i - 2] - (8 * y[i - 1]) + (8 * y[i + 1]) - y[i + 2])/(12 * (x[i + 1] - x[i]))
    dydx[0] = (y[1]-y[0])/(x[1]-x[0]) #forward difference
    dydx[1] = (y[2]-y[1])/(x[2]-x[1]) #forward difference
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2]) #backward diference
    dydx[-2] = (y[-2]-y[-3])/(x[-2]-x[-3]) #backward diference
    return dydx

def finiteDifference(x,y):
    """Input array x and y(x).
       Return the derivative of y with respect to x using the center difference method."""
    dydx = np.zeros(y.shape, float)
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:]-x[:-2]) #center difference
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])  #forward difference for first element
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])  #backward diference for last element
    return dydx
