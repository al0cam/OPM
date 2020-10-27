import sympy as sp
import numpy as np
import math
x = sp.Symbol('x')
p=5*x**4+6*x**3-6*x**2+4*x-8
razvoj=p.series(x,-1) #uvijek se stavlja razliciti predznak
razvoj
u=sp.Symbol('u')
raz=razvoj.subs({x:u-1}) #uvijek se stavljda razliciti predznak
raz
print(raz)
