import numpy as np
import scipy as sp
import scipy.interpolate as spi
import matplotlib.pyplot as plt
import pylab


x_koordinate=[-2, -1, 1, 2]
y_koordinate=[0, 1, 2, 3.89]
polinom=spi.lagrange(x_koordinate,y_koordinate)
print('Polinomi:\n',polinom)

xp=np.arange(-2.5,2.5,0.01)
yp=polinom(xp)

plt.figure(figsize=(6,5))
plt.grid(True)
plt.plot(xp,yp,'b-',x_koordinate,y_koordinate,'ro',markersize=8,linewidth=2)
plt.show()
