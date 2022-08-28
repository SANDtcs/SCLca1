from sympy import *
import math




#bisection method

def sub(expr,value):
    val=expr.subs(x,value)
    return val

def bisection(x0,x1,e):
    step = 1
    print('\n\n*** BISECTION METHOD IMPLEMENTATION ***')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, sub(e,x2)))

        if sub(e,x0) * sub(e,x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step = step + 1
        condition = abs(sub(e,x2)) > 0.001

    print('\nRequired Root is : %0.8f' % x2)


x1=1
x2=2
x,y = symbols('x y')
expr=x*x*x - x - 2
bisection(x1, x2, expr)




# Regula Falsi Method
def regula_false(f, limit):
    a = limit[0]
    b = limit[1]

    if f.subs(x, a) < 0:
        pass
    else:
        temp = b
        b = a
        a = temp

    h = float(abs(f.subs(x, a)) * (b - a)) / float(abs(f.subs(x, a)) + abs(f.subs(x, b)))
    t = float(a + h)

    while f.subs(x, t) > 0.00001 or f.subs(x, t) < -0.00001:
        print("t =", t, "\nf(t) =", f.subs(x, t), end = "\n\n")
        if f.subs(x, t) < 0:
            a = t
        else:
            b = t

        h = float(abs(f.subs(x, a)) * (b - a)) / float(abs(f.subs(x, a)) + abs(f.subs(x, b)))
        t = a + h

    print("SOLUTION\nx = {x}\nf(x) = {fx}".format(x = t, fx = f.subs(x, t)))



f = 3*x + cos(x) - x
limit = [-1, 0]

regula_false(f,limit)



#Fixed point Iteration method
def f(x):
    return pow(x, 3) - 7*pow(x, 2) - 8*x - 3

def g(x):
    return 3*pow(x, 2) - 14*x - 8

def fixed_point_iteration(f, limit):
    a = float(limit[0])
    b = float(limit[1])

    phi = -(f - f.coeff(x, 1) * x) / f.coeff(x, 1)

    if diff(phi, x).subs(x, a) < 1 and diff(phi, x).subs(x, b) < 1:
        pass
    else:
        print("Cannot use Fixed Point Iteration Method")
        return

    t = float(a)

    while f.subs(x, t) > 0.0001 or f.subs(x, t) < -0.0001:
        print("t =", t, "\nf(t) =", f.subs(x, t), end = "\n\n")
        t = phi.subs(x, t)

    print("SOLUTION\nx = {x}\nf(x) = {fx}".format(x = t, fx = f.subs(x, t)))

fixed_point_iteration(f,limit)








# Newton rhapson method
def newton_raphson(f, limit):
    a = limit[0]
    b = limit[1]
    t = float(a + b) / 2

    while f.subs(x, t) > 0.001 or f.subs(x, t) < -0.001:
        print("t =", t, "\nf(t) =", f.subs(x, t), end = "\n\n")
        t = t - f.subs(x, t) / diff(f, x).subs(x, t)

    print("SOLUTION\nx = {x}\nf(x) = {fx}".format(x = t, fx = f.subs(x, t)))



f = 3*x + cos(x) - x
limit = [-1, 0]

newton_raphson(f,limit)




