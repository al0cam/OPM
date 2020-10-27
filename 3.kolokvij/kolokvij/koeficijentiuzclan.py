import sympy as sp
import numpy as np
import math
x = sp.Symbol('x')

print(sp.interpolate([(-8.8,5.05), (-2.86,-3.89), (9.1,8.73), (9.76,0.21)],x))
