import sympy as sp
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import pylab 
import scipy.interpolate as scip
import math
from mpl_toolkits.mplot3d import Axes3D
x,y,z,t,u,v=sp.symbols('x y z t u v',real=True)
F=y*pow((85*x+17*y), 1/2)+x*pow((89*x+76*y), 1/3)
print(F, "\n")
Fx=F.diff(x)
Fy=F.diff(y)
Fx,Fy
Fx0=Fx.evalf(subs={x:4,y:93}) #tocka
Fy0=Fy.evalf(subs={x:4,y:93})
prirast_apr=Fx0*(0.02)+Fy0*(-0.2) #diferencijali
print(prirast_apr)
rj = round(prirast_apr,5)
print(rj)
