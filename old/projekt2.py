from scipy.sparse import linalg as ln
from scipy.sparse import csc_matrix as c
import numpy as n
import math


def unos():#unos ranga matrice
    print()
    rang = int (input('Rang matrice: '))
    print(rang)
    return rang
	#kraj unosa

def punjenje(rang):#punjenje matrice s vrijednostima
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
	#kraj punjenja

def stvori_A(B):#pretvaranje matrice prethodno stvorene s punjenjem u matricu A
    A = c(B)
    #print(A)

    return A
	#kraj stvaranja A

def stvori_x0(rang):#stvaranje matrice x0 koja je pocetna iteracija
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
	#kraj stvaranja matrice x0

def stvori_b(rang,B):#stvaranje vektora b
    print('Stvaranje b:\n')
    while 1:
        print("Samo jedinice-1\n Samo nule-2\n Slobodni koeficijenti-3\n Vlastiti unos-4\n")
        puni = int(input())
        if puni > 0 and puni < 5:
            break
    
    if puni == 1:
        b=n.reshape([1]*rang,(rang,1))
    elif puni == 2:
        b=n.reshape([0]*rang,(rang,1))
    elif puni == 3:
        b=B[:,rang-1]
    else:
        b=n.reshape([0]*rang,(rang,1))
        for i in range(rang):
            print("unesite [",i,"] broj:")
            b[i] = int(input())

    #print('b',b)

    return b
	#kraj stvaranja vektora b

def ispis_oblika(A,b,x0):#ispis oblika svih matrica i vektora koji se koriste
    print('A', A.shape, type(A))
    print('b', b.shape, type(b))
    print('x0', x0.shape, type(x0))
	#kraj ispisa svih oblika

def izracun_najbrzeg_silaska(A,b,x0):#izracun najbrzeg silaska uz prethodno definirane elemente, sadrzi ispis
    x=ln.minres(A,b,x0,0.0,1e-16,5)
    x=x[0]
    print("\nRezultat je\n")
    print(x,'\n')
	#kraj izracuna 

#main
#pozivi funkcija
rang = unos()
B = punjenje(rang) 
A = stvori_A(B)
x0 = stvori_x0(rang)
b = stvori_b(rang,B)
ispis_oblika(A,b,x0)
izracun_najbrzeg_silaska(A,b,x0)








