def f(x): 

    return 6 * pow(x, 4) + 4 * pow(x, 3) - pow(x, 2) - x - 10 

def df(x): 

    return 24 * pow(x, 3) + 12 * pow(x, 2) - 2 * x - 1 

def df2(x): 

    return 72 * pow(x, 2) + 24 * x - 2 

a = -2. 

b = -1 / 2 

eps = 0.001 

def kombinov(a, b, eps): 

    if (df(a) * df2(a) > 0): 

        a0 = a 

        b0 = b 

    else: 

        a0 = b 

        b0 = a 

    ai = a0 

    bi = b0 

    while abs(ai - bi) > eps: 

        ai_1 = ai - f(ai) * (bi - ai) / (f(bi) - f(ai)) 

        bi_1 = bi - f(bi) / df(bi) 

        ai = ai_1 

        bi = bi_1 

    x = (ai_1 + bi_1) / 2 

    return print('Rozvyazok po kombinovanomu metodu  x = ', x) 

kombinov(a, b, eps) 