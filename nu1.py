import numpy as np 

import math 

from scipy.misc import derivative 

def f(x): 

    return 6*pow(x,4)+4*pow(x,3)-pow(x,2)-x-10 

a=-2. 

b=-1/2 

eps=0.001 

def newton(a,b,eps): 

    df2 = derivative(f,b,n=2) 

    if (f(b)*df2>0): 

        xi = b 

    else: 

        xi = a 

    df = derivative(f, xi, n=1) 

    xi_1 = xi - f(xi)/df 

    while (abs(xi_1 - xi) > eps): 

        xi = xi_1 

        xi_1 = xi - f(xi) / df 

        return print('Rozvyazok po metodu Newtona* x = ', xi_1) 

newton(a, b, eps) 