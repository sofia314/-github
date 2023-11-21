#Обчислення інтеграла методом Симпсона 

import numpy as np 

from scipy import integrate 

 

# Задаємо функцію, яку необхідно інтегрувати 

def f(x): 

 return np.tan(x**2) / (x**2+1) 

 

# Задаємо межі інтегрування та початкову кількість розбиттів 

a=0.2 

b=1 

n=8 

 

# Обчислюємо значення інтегралу методом Симпсона 

def simpson_rule(f, a, b, n): 

    h= (b-a) /n 

    integr=f(a) +f(b) 

    for i in range(1,n): 

       k=a+i*h 

       ifi%2==0: 

          integr+=2*f(k) 

       else: 

          integr+=4*f(k) 

    integr*=h/3 

    return integr 

 

# Обчислюємо значення інтегралу методом Сімпсона з точністю 0.001 

integral1=simpson_rule(f, a, b, n) 

n*=2 

integral2=simpson_rule(f, a, b, n) 

while abs(integral2-integral1) /15>0.0001: 

    integral1=integral2 

    n*=2 

    integral2=simpson_rule(f, a, b, n) 

# Виводимо результат 

print("Simpsone method:", round(integral2, 4)) 

v,err=integrate.quad(f,a,b)#Перевірка 

print("Check for the simpsone method= ",round(v, 4)) 

 