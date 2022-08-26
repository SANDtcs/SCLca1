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
def f(x):
    return 3*x - math.cos(x) - 1

print('\n\n*** Regula Falsi METHOD IMPLEMENTATION ***')
a=0
b=1

h = (abs(f(a))*(b-a))/(abs(f(a)) + abs(f(b)))

while(h > 0.001):
    a = a+h
    h = (abs(f(a))*(b-a))/(abs(f(a)) + abs(f(b)))
    
print(f(a))
print(a)




#Fixed point Iteration method
def f(x):
    return pow(x, 3) - 7*pow(x, 2) - 8*x - 3

def g(x):
    return 3*pow(x, 2) - 14*x - 8

def FixedPointiteration(x0,e,N):
    print('\n\n*** ITERATION TABLE ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
       
        x1 = x0 - f(x0)/g(x0)
        print('Iteration-%d, x1 = %0.4f and f(x1) = %0.4f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
       
        if step > N:
            flag = 0
            break
       
        condition = abs(f(x1)) > e
   
    if flag==1:
        print('\nRequired root is: %0.6f' % x1)
    else:
        print('\nNot Convergent.')

x0 = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))
N = int(input('Maximum Step: '))
FixedPointiteration(x0,e,N)








# Newton rhapson method
def derivative(value,expr):
    
    expr_diff = diff(expr, x)
    val=expr_diff.subs(x,value)
    return val


def function(value,expr):
    
    val=expr.subs(x,value)
    return val


def newtonRaphson( x , expr):
    
    h = function(x, expr) / derivative(x, expr)
    while abs(h) >= 0.0001:
        h = function(x, expr) / derivative(x, expr)
         
        x = x - h
        print("The value of the root is : ","%.4f"% x)



x,y = symbols('x y')

z=12
expr=x**3 - 5*x - 9

newtonRaphson(z,expr)


