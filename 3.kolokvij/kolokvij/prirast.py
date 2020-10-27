import sympy as sp
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from pylab import *
import scipy.interpolate as scip
import math
from mpl_toolkits.mplot3d import Axes3D
x,y,z,t,u,v=sp.symbols('x y z t u v',real=True)
F=x*pow((35*x+16*y), 1/2)-y*pow((76*x+66*y), 1/3)
print(F, "\n")
Fx=F.diff(x)
Fy=F.diff(y)
Fx,Fy
Fx0=Fx.evalf(subs={x:28,y:65}) #tocka
Fy0=Fy.evalf(subs={x:28,y:65})
prirast_apr=Fx0*(-0.08)+Fy0*(0.03) #diferencijali
print(prirast_apr)
rj = round(prirast_apr,5)
print(rj)
