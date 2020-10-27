import numpy as np
import scipy as sp
import scipy.interpolate as spi
import matplotlib.pyplot as plt
import pylab

tocka=np.poly1d([-2,3,4,-5,1,2,8,12])
nul_real=np.extract(tocka.r.imag==0, tocka.r)
only_real = lambda x: x.real
vector_real = np.vectorize(only_real)
nul_real=vector_real(nul_real)
print(nul_real)

x1=np.arange(-1.5,2.2,0.04)
y1=tocka(x1)

plt.figure(figsize=(7,6))
plt.grid(True)
plt.xlim(-1.6,2.3)
plt.ylim(-15,45)
plt.hlines(0,-1.6,2.3)
plt.vlines(0,-15,45)
plt.plot(x1,y1,'b-',linewidth=2)
plt.plot(nul_real,[0,0,0],c='yellow',marker='h',ls='',ms=7,markeredgecolor='k')
plt.show()