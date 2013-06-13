def LinearLeastSquaresFit(x,y):
    """Take in arrays representing (x,y) values for a set of linearly varying data and perform a linear least squares regresstion.
    Return the resulting slope and intercept parameters of the best fit line with their uncertainties."""
    
    n = len(x)
    
    ax = sum(x)/n
    ay = sum(y)/n
    axsq = sum(x**2)/n
    axy = sum(x * y)/n
    
    slope = (axy - (ax * ay)) / (axsq - ax**2.0)
    intercept = ((axsq * ay) - (ax * axy)) / (axsq - ax**2.0)
    
    adsq = sum((y - (slope * x) - intercept)**2)/n
    
    slerr = (adsq/((n - 2) * (axsq - ax**2.0)))**(0.5)
    interr = ((adsq * axsq)/((n-2) * (axsq - ax**2.0)))**(0.5)
    
    return slope, intercept, slerr, interr

def WeightedLinearLeastSquaresFit(x, y, w):
    """Take in arrays representing (x, y) values for a set of linearly varying data and an array of weights w.
    Perform a weighted linear least squares regression.
    Return the resulting slope and intercept parameters of the best fit line with their uncertainties.

    If the weights are all equal to one, the uncertainties on the parameters are calculated using the non-weighted least squares equations."""
    
    sw = 1 / (w)**2
    
    if sum(sw)/len(sw) == 1:
        n = len(x)
        ax = sum(x)/n
        ay = sum(y)/n
        axsq = sum(x**2)/n
        axy = sum(x * y)/n
        slope = (axy - (ax * ay)) / (axsq - ax**2.0)
        intercept = ((axsq * ay) - (ax * axy)) / (axsq - ax**2.0)
    else:
        slope = (sum(sw) * sum(sw * x * y) - sum(sw * x) * sum (sw * y)) / (sum(sw) * sum(sw * x**2) - (sum(sw * x))**2)
        intercept = (sum(sw * x**2) * sum(sw * y) - sum(sw * x) * sum(sw * x * y)) / (sum(sw) * sum(sw * x**2) - (sum(sw * x))**2)
    
    slerr = (sum(sw) / (sum(sw) * sum(sw * x**2) - (sum(sw * x))**2))**(0.5)
    interr = (sum(sw * x**2) / (sum(sw) * sum(sw * x**2) - (sum(sw * x))**2))**(0.5)
    
    return slope, intercept, slerr, interr
