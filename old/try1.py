from scipy.sparse import linalg as ln
from scipy.sparse import csc_matrix as c
import numpy as n
import math


def unos():
    print()
    rang = int (input('Rang matrice: '))
    print(rang)
    return rang

def punjenje(rang):
    while 1:
        print("Samo jedinice-1\n Samo nule-2\n Vlastiti unos-3\n")
        puni = int(input())
        if puni > 0 and puni < 4:
            break

    if puni == 1:
        B = [1]*(rang**2)
        B = n.reshape(B,(rang,rang))
    elif puni == 2:
        B = [0]*(rang**2)
        B = n.reshape(B,(rang,rang))
    else:
        B = [1]*(rang**2)
        B = n.reshape(B,(rang,rang))
        for i in range(rang):
            for j in range(rang):
                print("unesite [",i,"][",j,"] broj:")
                B[i][j] = int(input())

    return B

def stvori_A(B):
    A = c(B)
    #print(A)

    return A

def stvori_x0(rang):
    print('Stvaranje x0:\n')
    while 1:
        print("Samo jedinice-1\n Samo nule-2\n Vlastiti unos-3\n")
        puni = int(input())
        if puni > 0 and puni < 4:
            break
    
    if puni == 1:
        x0=n.reshape([1]*rang,(rang,1))
    elif puni == 2:
        x0=n.reshape([0]*rang,(rang,1))
    else:
        x0=n.reshape([0]*rang,(rang,1))
        for i in range(rang):
            print("unesite [",i,"] broj:")
            x0[i] = int(input())
    
    #print('x0',x0)

    return x0

def stvori_b(rang,B):
    print('Stvaranje b:\n')
    while 1:
        print("Samo jedinice-1\n Samo nule-2\n Vlastiti unos-3\n")
        puni = int(input())
        if puni > 0 and puni < 4:
            break
    
    if puni == 1:
        b=n.reshape([1]*rang,(rang,1))
    elif puni == 2:
        b=n.reshape([0]*rang,(rang,1))
    else:
        b=n.reshape([0]*rang,(rang,1))
        for i in range(rang):
            print("unesite [",i,"] broj:")
            b[i] = int(input())

    #print('b',b)

    return b

def ispis_oblika(A,b,x0):
    print('A', A.shape, type(A))
    print('b', b.shape, type(b))
    print('x0', x0.shape, type(x0))

def izracun_najbrzeg_silaska(A,b,x0):
    x=ln.minres(A,b,x0,0.0,1e-16,5)
    x=x[0]
    print("\nRezultat je\n")
    print(x,'\n')

#main
rang = unos()
B = punjenje(rang) 
A = stvori_A(B)
x0 = stvori_x0(rang)
b = stvori_b(rang,B)
#ispis_oblika(A,b,x0)
izracun_najbrzeg_silaska(A,b,x0)








