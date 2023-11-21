def hord (a,b, eps) -> None: #метод хорд

if (f(a)*derivative(f,a,n=2)>0) :

x0: Any=a

xi: Any=b
else:


X0: Any=b

xi: Any=a

xi_1: Any=xi-(xi-x0)*f(xi)/(f(xi)-f(x0))

while (abs (xi_1-xi)>eps):

xi: Any=xi_1

xi_1: Any=xi-(xi-x0)*f(xi)/(f(xi)-f(x0))

print('x= ', round (xi_1,5) ,
Chord method')