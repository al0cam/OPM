import platform
platform.platform()
platform.python_version()

import numpy as np
import numpy.linalg as LA
import math

import sympy
#from sympy import init_printing
#from sympy import Point3D


#zbroj radij vektora
print()
A=sympy.Point3D(1,-2,7)
B=sympy.Point3D(9,1,-5)
print("zbroj radij vektora: ",A+B,"\n")

#skaliranje radij vektora
print("skaliranje radij vektora: ",A.scale(2,5,-3),"\n")

#skalarni produkt radij vektora
print("skalarni produkt radij vektora: ",A.dot(B),"\n")

#vektor odredjen s dvije tocke
A=sympy.Point3D(2,3,1)
B=sympy.Point3D(-4,2,5)
print("vektor odredjen s dvije tocke: ",A.direction_ratio(B),"\n")

#udaljenost tocaka
A=sympy.Point3D(1,3,-2)
B=sympy.Point3D(6,-9,1)
print("udaljenost tocaka: ",A.distance(B))
print("udaljenost tocaka decimale: ",round(A.distance(B),10),"\n")

#kolinearnost tocaka
A=sympy.Point3D(1,2,3)
B=sympy.Point3D(4,0,-5)
C=sympy.Point3D(37/16,9/8,-1/2)
D=sympy.Point3D(0,-3,2/3)
print("samo ispis C: ",C)
print("ispis C decimalno :",C.evalf())
print("tocke A, B i C su kolinearne: ",sympy.Point3D.are_collinear(A,B,C))
print("tocke A, B i D nisu kolinearne: ",sympy.Point3D.are_collinear(A,B,D),"\n")

#kosinus smjera radij vektora
A=sympy.Point3D(1,-2,3)
O=sympy.Point3D(0,0,0)
print("kosinus smjera radij vektora: ",O.direction_cosine(A),"\n")

#kosinus smjera vektora odredjenog s dvije tocke
A=sympy.Point3D(1,4,-2)
B=sympy.Point3D(0,-2,1)
print("kosinus smjera vektora odredjenog s dvije tocke: ",A.direction_cosine(B),"\n")

#zadavanje ravnine pomocu tocke i vektora normale
rav=sympy.Plane(sympy.Point3D(1,2,1),(-2,3,-1))
print("Ravnina uz pomoc tocke i vektora normale: ",rav)

#opci oblik jednadzbe ravnine
print("opci oblik jednadzbe ravnine: ",rav.equation())

#slucajana tocka u ravnini
ranT=rav.random_point()
print("Slucajna tocak u ravnini: ",ranT)

from sympy import var
#parametarska jednadzba ravnine
u,v=var('u v')
par=rav.arbitrary_point(u,v)
print("parametarska jednadzba ravnine: ",par)

#Točka u ravnini koja se dobije za  u=2,   v=1
Tp=par.subs({u:2,v:1})
print("Točka u ravnini koja se dobije za  u=2,   v=1: ",Tp)

#dobiavnje parametara za danu tocku koja lezi u ravnini
print("dobiavnje parametara za danu tocku koja lezi u ravnini: ",rav.parameter_value(Tp,u,v),"\n")

#Zadavanje ravnine pomoću tri nekolinearne točke
T1=sympy.Point3D(1,2,1)
T2=sympy.Point3D(-1,0,3)
T3=sympy.Point3D(-2,-1,5)
rav=sympy.Plane(T1,T2,T3)
print("Zadavanje ravnine pomoću tri nekolinearne točke: ",rav)

#vektor normale
print("vektor normale: ",rav.normal_vector,"\n")

#udaljenost tocke od ravnine
rav=sympy.Plane(sympy.Point3D(5,0,0),(2,-1,3))
T=sympy.Point3D(1,-2,4)
print("udaljenost tocke od ravnine: ",rav.distance(T))

#tocka t ne lezi u ravnini
print("tocka t ne lezi u zadanoj ravnini: ",rav.is_coplanar(T),"\n")

#medjusobni polozaj ravnina
rav1=sympy.Plane(sympy.Point3D(-5/2,0,0),(2,3,-4))
rav2=sympy.Plane(sympy.Point3D(1,0,0),(1,-2,2))
kut=rav1.angle_between(rav2)
print("kut izmedju normali ravnina: ",kut)

print("kut izmedju normali u radijanima: ",round(kut,10))
kut2=(round(kut,10)*180/np.pi)
print("kut izmedju normali u stupnjevima: ",kut2)

#ravnine paralelne
print("jesu li ravnine paralelne: ",rav1.is_parallel(rav2))

#ravnine okomite
print("jesu li ravnine okomite: ", rav1.is_perpendicular(rav2))


