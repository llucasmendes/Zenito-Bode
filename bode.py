import sympy
from sympy import *
from control import matlab
import matplotlib.pyplot as plt

def freqResponse(Ts,*args,**kwargs):
    num = Poly(Ts.as_numer_denom()[0],s).all_coeffs()
    den = Poly(Ts.as_numer_denom()[1],s).all_coeffs()
    tf = matlab.tf(map(float,num),map(float,den))
    matlab.bode([tf],*args,**kwargs)
    plt.show()

sympy.init_printing()
s = Symbol('s')
G = 1
while G != 0:
	G = input('H(s)= ')
	#sympy.core.power.Pow
	sympify(G).is_real

	print"\n\t", G

	#G.simplify()

	print'\n\t', G.simplify()

	freqResponse(G)
