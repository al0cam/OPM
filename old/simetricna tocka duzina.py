import platform
platform.platform()
platform.python_version()

import numpy as np
import numpy.linalg as LA
import math

import sympy
from sympy import var

H=sympy.Point3D(-69.2,89.23,70.43)
tockanax=-(-33.21/80.86)
ravnina=sympy.Plane(sympy.Point3D(tockanax,0,0),(80.86,-66.12,-18.29))
presjeknaravnini=ravnina.projection(H)
Hc=presjeknaravnini+H.direction_ratio(presjeknaravnini)
E=sympy.Point3D(-32.6,67.92,-51.91)
print(round(Hc.distance(E),5))


