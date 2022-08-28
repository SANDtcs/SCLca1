import numpy as np

# power method

def normalize(x):
  max = abs(x).max()
  newX = x / x.max()
#   print(max, newX)

  return max, newX

  # matrix = np.array([[2, 3], [4, 10]])
matrix = np.array([[2, 1], [0, -4]])

order = len(matrix)
x = np.ones((order, 1), dtype = int)

for i in range(8):
  x = np.dot(matrix, x)
  l, x = normalize(x)

print("Eigenvalue:", l)
print("Eigenvector:", x)




#inverse power
from sympy import *
import numpy as np

def eigenValues(matrix):
  l = symbols('lambda')
  order = len(matrix)
  I = np.identity(order, dtype = int)
  lI = I * l
  expr = Matrix(lI - matrix).det()
  eigValues = solve(expr)

  return eigValues

matrix = [[10, -8, -4], [-8, 13, 4], [-4, 5, 4]]
eValues = eigenValues(matrix)
# minE = min(eValues)
minE = 1.9

order = len(matrix)
I = np.identity(order, dtype = int)
lI = I * minE
x = np.ones((order, 1), dtype = int)
mu = 0
v = 0

for i in range(5):
    y = np.linalg.inv(matrix - lI) * x
    mu = np.amax(y)
    v = minE + 1 / mu
    x = (1 / mu) * y

print(v)