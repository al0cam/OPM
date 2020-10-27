import numpy as np
import scipy as sp
import matplotlib
import pylab


#main

#ubacivanje polinoma
f=np.poly1d([1,0,-3,0,-5,0])
print('Polinom f: ','\n',f,"\n")

g=np.poly1d([1,-1,1])
#ispis polinoma
print('Polinom g: ','\n',g,'\n')

#ako zelimo neku drugu varijablu ujmesto x
g1=np.poly1d([1,-1,1],variable='u')
print('Polinom g1: ','\n',g1,'\n')

#koeficijenti polinoma
print('Koeficijenti polinoma f:','\n',f.c)

#koeficijent uz potenciju
print('Koeficijent uz potenciju 3 polinoma f:','\n',f[3])

#stupanj polinoma
print('Stupanj polinoma f:','\n',f.o)

#racunanje vrijednost polinoma u tocki
print('Vrijednost polinoma f u tocki 3:','\n',f(3))

#derivacija polinoma
print('Derivacija polinoma f:','\n',f.deriv())

#derivacija viseg reda
print('2. Derivacija polinoma f','\n',f.deriv(2))

#integral polinoma
print('Integral polinoma f:','\n',f.integ())

#zbrajanje polinoma
print('Zbrajanje polinoma f i g:','\n',f+g)

#oduzimanje polinoma
print('Oduzimanje polinoma f i g:','\n',f-g)

#mnozenje polinoma
print('Mnozenje polinoma f i g:','\n',f*g)

#potenciranje polinoma
print('Potenciranje polinoma f:','\n',f**2)

#polinom koji smo izracunali nekak
print('Polinom f**3*g+2*f:','\n',f**3*g+2*f)

#suma koeficijenata polinoma
print('Polinom f**3*g+2*f:','\n',(f**3*g+2*f)(1))

#dijeljenje polinoma
kvocijent, ostatak=f/g
print('Kvocijent polinoma f i g:','\n',kvocijent)
print('Ostatak polinoma f i g:','\n',ostatak)

#nultocka polinoma
print('Nultocka polinoma f:','\n',f.r)

#samo realne nultocke
nul_real = np.extract(f.r.imag == 0, f.r)
print('Realne nultocke od f:\n',nul_real)

#lijepsi zapis nultocke samo realne
only_real = lambda x: x.real
vector_real = np.vectorize(only_real)
print('Realne nultocke od f lijepi zapis:\n',vector_real(nul_real))
