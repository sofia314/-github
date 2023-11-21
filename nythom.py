det
f(x) :
return 6 * pow(x, 4) + 4 * paw(x, 3) - pow(x, 2) - x - 10 def df(x):
return 24 * paw(x, 3) + 12 * paw(x, 2) - 2 * × - 1
def df2(x) :
return 72 * pow(x, 2) + 24 * × - 2
a= -2.
b= -1 / 2
eps = 0.001
def kombinov (a, b, eps):
if (df(a)*df2(a)> 0):
a0 = a
b0 = b
else:
a0= b
b0=a
ai= a0
bi = b0
while abs(ai - bi) > eps:
ai_1 = ai - f(ai) * (bi - ai) / (f(bi) - f(ai))
bi_1 = bi - f(bi) / df(bi)
ai = ai_1
bi = bi_1
x = (ai_1 + bi_1) / 2
return print ('Rozvyazok pe kombinevananu metadu
x = ', x)
kombinov (a, b,
eps)