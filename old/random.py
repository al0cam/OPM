from numpy.random import random
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve, minres

N = 10
A = csc_matrix( random(size = (N,N)) )
A = (A.T).dot(A) # force the matrix to be symmetric, as required by minres
x = csc_matrix( random(size = (N,1)) ) # create a solution vector
b = A.dot(x) # create the RHS vector

# verify shapes and types are correct
print('A', A.shape, type(A))
print('x', x.shape, type(x))
print('b', b.shape, type(b))

# spsolve function works fine
sol1 = spsolve(A, b)

# other solvers throw a incompatible dimensions ValueError
sol2 = minres(A, b.todense())