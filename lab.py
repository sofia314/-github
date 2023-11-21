def
rec(a, b, eps) -> None:
#метод половинного ділення
while (abs (a-b) > eps):
if f(a)*f((a+b)/2)<0:
b: Any = (a+b)/2
else:
a: Any = (a+b)/2
x: Any = (a+b)/2
print ('x= ', round (x,5), ' - Half division method*)