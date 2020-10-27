import platform
platform.platform()
platform.python_version()

import numpy as np
import numpy.linalg as LA
import math

import sympy as sp

M=sp.Matrix([[-4,9,-17,3,-2,-22],[2,-4,8,-1,2,10],[-2,0,-4,4,4,-2],[4,3,5,-8,-8,-2]])
N=M
M=M.T
M.columnspace()
print(M.rank())
print(M.rref())
print(N.rank())