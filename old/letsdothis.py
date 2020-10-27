import platform
platform.platform()
platform.python_version()

import numpy as np
import numpy.linalg as LA
import math

import sympy
from sympy import var


#Zadavanje ravnine pomoću tri nekolinearne točke
T1=sympy.Point3D(35,33,-46)
T2=sympy.Point3D(-36,-40,-44)
T3=sympy.Point3D(0,-11,48)
rav=sympy.Plane(T1,T2,T3)
print("Zadavanje ravnine pomoću tri nekolinearne točke: ",rav)

#dvije ravnine
pi1=sympy.Plane(sympy.Point3D(0.92857,0,0),(-14,7,-8))
print(pi1.equation())

pi2=sympy.Plane(sympy.Point3D(0,1.869565,0),(21,-23,32))
print(pi2.equation())

normala1=pi1.intersection(pi2)[0]
print(normala1.equation())
kut=rav.angle_between(normala1)
print(kut)
print(kut)
kut2=(round(kut,10)*180/np.pi)
print(round(kut2,5))


