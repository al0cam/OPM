import platform
platform.platform()
platform.python_version()

import numpy as np
import numpy.linalg as LA
import math


c=np.array([-55.43,39.51,-80.93])
p=np.array([-83.78,-93.07,68])
q=np.array([-9.99,30.71,67.81])

print("zbroj vektora: ")
zbroj=4.8*c-1.26*p
rez=(np.dot(np.dot(zbroj,q),zbroj)/math.pow(LA.norm(zbroj),2))
print(rez)

print("Duljina vektora: ")
print(round(LA.norm(rez),5))


a=np.array([-34.5,38.94,-88.15])
u=np.array([87.75,-48.77,56.58])

kut_rad=np.arccos(np.dot(a,u)/(LA.norm(a)*LA.norm(u)))
print(kut_rad)
print(round(kut_rad*180/math.pi,5))


a=np.array([-17.04,13.26,-16.82])
c=np.array([-16.03,21.55,29.56])
u=np.array([-1.65,25.47,15.9])

ua=np.cross(u,a)
cua=np.cross(c,ua)
print(round(LA.norm(cua),5))


c=np.array([-1.16,0.02,-8.14])
p=np.array([-9.93,-19.1,26.74])
u=np.array([3.23,-28.16,-2.19])

cp=c+p
print(cp)
cpu=cp+u
print(cpu)
print(round(LA.norm(cpu),5))

