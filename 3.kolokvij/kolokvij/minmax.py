import sympy as sp
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from pylab import *
import scipy.interpolate as scip
import math
from mpl_toolkits.mplot3d import Axes3D
x,y,z,t,u,v=sp.symbols('x y z t u v',real=True)

f= x**2-y**2-14*x+12*y
print(f, "\n")
fx=f.diff(x)
fy=f.diff(y)
stac=sp.solve([fx,fy],[x,y])
print("Stacionarna tocka: ", stac)

rj = f.evalf(subs={x:9, y:6}) # tu ide stacionarna tocka
print(rj)
a = f.evalf(subs={x:-3,y:-2}) # tu ide tocka A
print(a)
b = f.evalf(subs={x:12,y:8}) # tu ide tocka B
print(b)

# rjesenje globalnog minimuma je najmanja od te tri,
# globalnog maksimuma najveca od te tri