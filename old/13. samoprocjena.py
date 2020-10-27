import platform
platform.platform()
platform.python_version()
import numpy as np
import pylab
import math

p=np.poly1d([-8,3,1,6,-3])
razvoj=[p.deriv(k)(1)/math.factorial(k) for k in range(p.o+1)]
print(razvoj)