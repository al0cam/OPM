from scipy.sparse import linalg as ln
from scipy.sparse import csc_matrix as c
import numpy as n
import math
import matplotlib.pyplot as plt

broj=[]
def pisi(xk):
    broj.append(xk)

i=2
B = n.arange(1,10001).reshape(100,100)

for i in  range(100):
    for j in range(100):
        B[i][j]=B[i][j]**2        

A=c(B)


x0former=[0]*100
x0now=n.reshape(x0former,(100,1))
x0=x0now


b=B[:,99]
#b=n.array(b1)

print('A', A.shape, type(A))
print('x', x0.shape, type(x0))
print('b', b.shape, type(b))

x=ln.minres(A,b,x0,0.0,1e-8,None,None,pisi)
x=x[0]
print(x)
plt.ylim(10**(-8))
plt.plot(x)
plt.ylabel('some numbers')
plt.show()
