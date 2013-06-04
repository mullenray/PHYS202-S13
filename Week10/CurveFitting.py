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
