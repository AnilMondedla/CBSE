import numpy as np
import matplotlib.pyplot as plt
import math
from coeffs import *
import sympy as sym
x = sym.symbols('x')

A =np.array([x,2])
B =np.array([9,8])
AB = (A-B)
AB = np.transpose(AB)@(AB)
print(AB)
C = 100.0

S= list(sym.solveset(AB-C, x))
S = (int(S[0]),int(S[1]))
print(S)

A=np.array([S[0],2])
C=np.array([S[1],2])
x_AB = line_gen(A,B)
x_CB = line_gen(C,B)
#Plotting Line between A and B
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1-0.3), B[1] * (1-0.1) , 'B')
plt.plot(x_CB[0,:],x_CB[1,:],label='$CB$')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.1), C[1] * (1 - 0.1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()



