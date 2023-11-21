import numpy as np 

x=np.array([-2,-1,1,2], dtype=float) 

y=np.array([-26,-5,1,10], dtype=float) 

x_test = 0.5  

def lagrange_interpolation(x, y, x_test): 

    n = len(x) 

    p = np.zeros(n) 

    for i in range(n): 

        p_i = 1 

        for j in range(n): 

            if i!= j: 

                p_i*= (x_test - x[j])/(x[i] - x[j]) 

        p[i] = p_i 

    return np.dot(y, p)  

f_interp = lagrange_interpolation(x, y, x_test) 

print("Значення функції у точці x_test =", f_interp.round(4)) 