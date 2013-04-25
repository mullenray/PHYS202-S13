def pointPotential(x,y,q,posx,posy):
    """x,y are the point or points in space for which the electric potential is to be found.
    q is the charge
    posx, posy is the position of the charge in the plane

    returns the electric potential due to the charge"""
    k = 8.987551787 #(Nm^2)/C^2
    Vxy = ((k * q)/((x - posx)**2 + (y - posy)**2)**(1/2.0))
    return Vxy

def dipolePotential(x,y,q,d):
    """x,y are the point or points in space for which the electric potential is to be found.
    q is the charge
    d is the separation distance between the charges

    returns the electric potential due to the dipole"""
    V1 = pointPotential(x,y,q,abs(d),0.0)
    V2 = pointPotential(x,y,q,-abs(d),0.0)
    Vxy = V1 - V2
    return Vxy
