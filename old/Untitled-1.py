import platform
platform.platform()
platform.python_version()

import numpy as np
import numpy.linalg as LA
import math


v1=np.array([1,0,2])
v2=np.array([-2,0,1])
print("zbroj vektora: ")
print(v1+v2)

print("Oduzimanje vektora: ")
print(v1-v2)

print("Množenje vektora skalarom: ")
print(5*v1)

print("Linearna kombinacija vektora: ")
print(2/5*v1+7*v2)

print("Duljina vektora: ")
print(LA.norm(v1))
print(LA.norm(v2))
print(LA.norm(2/5*v1+7*v2))

print("Skalarni produkt vektora: ")
print(v1,v2)
print(np.dot(v1,v2))
print(np.dot(v2,v1))

print("Kut između vektora u radijanima: ")
kut_rad=np.arccos(np.dot(v1,v2)/(LA.norm(v1)*LA.norm(v2)))
print(kut_rad)

print("Kut između vektora u stupnjevima: ")
print(kut_rad*180/np.pi)

print("Kut od kosinusa: ")
kut=(np.dot(v1,v2)/(LA.norm(v1)*LA.norm(v2)))
print(kut)

print("Vektorski produkt vektora: ")
print(np.cross(v1,v2))
print(np.cross(v2,v1))
print("povrsina: ")
zad=np.cross(v1,v2)
povrsina=math.sqrt(math.pow(zad[0],2)+math.pow(zad[1],2)+math.pow(zad[2],2))
print(povrsina)

print("Mješoviti produkt vektora: ")
a=np.array([1,2,-6])
b=np.array([-3,2,7])
c=np.array([0,2,3])
print(np.dot(np.cross(a,b),c))




