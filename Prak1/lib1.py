#Praktikum 1 Numerische Integration

import math as ma

def R(f, a, b):
    return f((a + b)/2) * (b - a)

def T(f, a, b):
    return (f(a) + f(b))/2 * (b - a)

def S(f, a, b):
    return (b - a) / 6 * (f(a) + 4 * f((a+b)/2)+f(b))


def Rh(f, a, b, n):
    h = (b-a)/n
    erg = 0
    for i in range(0, n):
        erg += f((a+i*h)+h/2)
    return erg*h

def Th(f, a, b, n):
    h = (b-a)/n
    erg = 0
    for i in range(1, n):
        erg += f(a + i*h)
        
    return h*((f(a)+f(b))/2+erg)

def Sh(f, a, b, n):
    h = (b-a)/n
    erg1 = 0
    erg2 = 0
    for i in range(0, n):
        erg1 += f(a+i*h+h/2)
    for i in range(1, n):
        erg2 += f(a+i*h)
    return h/6 * (f(a)+f(b)+2*erg2+4*erg1)


def phi(x):
    return (ma.e**((-x**2)/2))/(ma.sqrt(2*ma.pi))

def Gauß(a, b):
    l = 40
    if a < -l:
        a = -l
    if b > l:
        b = l
       
    n = int(((abs(b - a) ** 5 * 1e10) / ((2880/3) * ma.sqrt( 2 * ma.pi ))) ** (1 / 4)) + 1
    print(a, b, n)
    return Sh(phi, a, b, n)

print("Gauß: ", Gauß(0, 1))
