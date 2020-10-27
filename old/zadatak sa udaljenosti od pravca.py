import platform
platform.platform()
platform.python_version()

import numpy as np
import numpy.linalg as LA
import math

import sympy
from sympy import var

pravac=sympy.Line3D(sympy.Point3D(66.5,-33.93,-93.39),(41.22,24.1,69.82))
tocka=sympy.Point3D(19.43,-25.51,32.48)
print(round(pravac.distance(tocka),5))

