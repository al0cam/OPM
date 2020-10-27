import platform
platform.platform()
platform.python_version()

import numpy as np
import numpy.linalg as LA
import math

import sympy
from sympy import var

H=sympy.Point3D(18,-95,56)

pravac1=sympy.Line3D(sympy.Point3D(10,-27,24),sympy.Point3D(-17,-65,63))
pravac2=sympy.Line3D(sympy.Point3D(41,54,86),sympy.Point3D(43,129,32))

s1=sympy.Matrix(pravac1.direction_ratio)
s2=sympy.Matrix(pravac2.direction_ratio)

nor=s1.cross(s2)
nor_pi1=s1.cross(nor)

pi1=sympy.Plane(sympy.Point3D(10,-27,24),nor_pi1)

nor_pi2=s2.cross(nor)
pi2=sympy.Plane(sympy.Point3D(41,54,86),nor_pi2)

normala=pi1.intersection(pi2)[0]

N1=normala.intersection(pravac1)[0]
N2=normala.intersection(pravac2)[0]

pravaca=sympy.Line3D(H,N1)
pravacb=sympy.Line3D(H,N2)

vektora=sympy.Matrix(pravaca.direction_ratio)
vektorb=sympy.Matrix(pravacb.direction_ratio)
cross=vektora.cross(vektorb).norm()
print(round(cross,5))



