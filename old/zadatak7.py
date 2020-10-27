from scipy.sparse import linalg as ln
from scipy.sparse import csc_matrix as c
import numpy as n
import math
import matplotlib.pyplot as plt


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

broj=[]
def neka_vrijednost(vrijednost):
    broj.append(vrijednost)
    #print(vrijednost)

def izracun_najbrzeg_silaska(A,b,x0):
    x=ln.minres(A,b,x0,0.0,1e-8,None,None,neka_vrijednost,1)
    x=x[0]
    print("\nRezultat je\n")
    print(x,'\n')
    
    return x

def izracun_residuala(broj,b):
    residuali=[]
    for i in broj:
        residuali.append(sum(i)/sum(b[:]))
        
    

    
    return residuali


def crtanje_grafa(x,rang):
    #r = [1]*(rang)
    #r = r-x
    #plt.ylim(10**(-8))
    plt.plot(x)
    plt.ylabel('greska')
    plt.xlabel('iteracije')
    plt.show()



#main
#rang = unos()
#B = punjenje(rang) 
rang = 100
B = n.arange(1,10001).reshape(100,100)

for i in  range(100):
    for j in range(100):
        B[i][j]=B[i][j]**2  


A = stvori_A(B)
A = A.transpose()
x0 = stvori_x0(rang)

#b=n.array(B[:,99])
b = stvori_b(rang,B)
#ispis_oblika(A,b,x0)
x = izracun_najbrzeg_silaska(A,b,x0)
residuali=izracun_residuala(broj,b)
brojac=0
for i in broj:
    brojac=brojac+1
print('brojac:', brojac)
crtanje_grafa(residuali,brojac)









