import sympy as sp
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import pylab
import scipy.interpolate as scip
import math
from mpl_toolkits.mplot3d import Axes3D
x,y,z,t,u,v=sp.symbols('x y z t u v',real=True)
f=(-47*x+44*y)*sp.Rational(6.04)**(-x**2-y**2)
print(f, "\n")
fx=f.diff(x)
fy=f.diff(y)
stac=sp.solve([fx,fy],[x,y])
stac
stac1=stac[0]
stac2=stac[1]
stac1 = tuple(map(lambda x: sp.N(x), stac1))
stac1
stac2=tuple(map(lambda x: sp.N(x), stac2))
stac2
hess_f=sp.hessian(f,[x,y])
hess_f
H1=hess_f.evalf(subs={x:stac1[0],y:stac1[1]})
H1
H1.det()
H2=hess_f.evalf(subs={x:stac2[0],y:stac2[1]})
H2
H2.det()
rj = f.evalf(subs={x:stac2[0],y:stac2[1]}) # x:stac2 y:stac2 - maximum
print(rj)
x = round(rj, 5)
print(x)
