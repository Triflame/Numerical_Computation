# -*- coding: utf-8 -*-

from __future__ import division
import sympy as sp
Lab05 = open("Lab05.txt", "w")


def Newton (f, x_0, epsilon, MAXREPT):
    print ("The initial value x is: %.1f\n" % x_0)
    x = sp.Symbol("x")
    x_k1 = x_k = x_0
    df = sp.diff(f, x)
    for i in range (MAXREPT):
        df0 = float(df.subs(x, x_k1))
        if df0 == 0 :
            print ("Step: %d Please choose a corret initial value!\n" % (i+1))
            return 0, -1
        f0  = float(f.subs(x, x_k1))
        x_k1 = x_k - f0 / df0
        if abs (x_k1 - x_k) < epsilon and i < MAXREPT :
            print ("Step: %d The root is x = %.12e\n" % (i+1, x_k1))
            return x_k1, i+1
        x_k = x_k1
    return x_k1, i+1


def Secant (f, x_0, x_1, epsilon, MAXREPT):
    print ("The initial value x is: %.1f, %.1f\n" % (x_0, x_1))
    x_k  = x_0
    x_k1 = x_1
    for i in range (MAXREPT):
        fx_k   = float(f.subs(x, x_k))
        fx_k1  = float(f.subs(x, x_k1))
        if fx_k == fx_k1 :
            print ("Not find the root!\n")
            return x_k1, 1
        x_k2 = x_k1 - fx_k1*(x_k1 - x_k) / (fx_k1 - fx_k)
        if abs (x_k1 - x_k2) < epsilon and i < MAXREPT :
            print ("Step: %d The root is x = %.12e\n" % (i+1, x_k1))
            return x_k2, i+1
        elif abs (x_k1 - x_k2) >= epsilon and i == MAXREPT-1:
            print ("Not find the root!\n")
            return 0, MAXREPT
        x_k  = x_k1
        x_k1 = x_k2
    return x_k2, i+1


x = sp.Symbol("x")
f = x**3 / 3 - x
epsilon = 1.0e-10
MAXREPT = 10000
x_0 = [-3.0, -1.5, 0.1, 0.2, 0.75, 1.0, 2.0, 6.0]


print ("Newton iteration\n")
Lab05.write ("Newton iteration\n\n")
for i in range(7):
    root, N = Newton (f, x_0[i], epsilon, MAXREPT)
    Lab05.write ("%4.1f , %19.12e , %d\n" % (x_0[i], root, N))
    
print ("Secant iteration\n")
Lab05.write ("\nSecant iteration\n\n")
for i in range(6):
    root, N = Secant (f, x_0[i], x_0[i+1], epsilon, MAXREPT)
    Lab05.write ("%4.1f, %4.1f , %19.12e , %d\n" % (x_0[i], x_0[i+1], root, N))
    
Lab05.close()

