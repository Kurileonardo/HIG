import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as constants


def Intensity(nu,T):
    c=constants.value("speed of light in vacuum")
    h=constants.value("Planck constant")
    k=constants.value("Boltzmann constant")
    nu=nu*c*100
    fact=h*nu/(k*T)
    In=h*nu**3/c**2*1/(np.exp(fact)-1)
    return In



def SI_to_Mjansky(value_SI):
    return value_SI/10e-26/1e6

data=np.loadtxt("IRCF.txt").T
nu=data[0]
I=data[1]
Ierr=data[3]

Intensity=SI_to
plt.plot(nu,Intensity(nu,5))
plt.show()
plt.errorbar(nu,I,Ierr)
plt.show()
