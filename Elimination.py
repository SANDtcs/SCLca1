print('\n\n*** GAUSS JORDAN ELIMINATION METHOD IMPLEMENTATION ***')

import math
def non_zero(row):
  for i in range(len(row)):
    if row[i] != 0:
      return i

def rref(matrix):
  rows = len(matrix)
  columns = len(matrix[0])
  non_zero_index = -1

  # Arrange the rows by leftmost non-zero entry
  matrix.sort(key = non_zero)
  for i in range(0, rows):
  # Making the first non-zero element 1
    for j in range(columns):
      if not math.isclose(matrix[i][j], 0.0):
        non_zero_index = j
        matrix[i] = [x / matrix[i][j] for x in matrix[i]]
        break

  # Making leading coefficient column corresponding values 0
    for j in range(rows):
      if j == i:
        continue
      else:
        ratio = matrix[j][non_zero_index] / matrix[i][non_zero_index]
        row = [x * ratio for x in matrix[i]]
        matrix[j] = [x - y for x, y in zip(matrix[j], row)]
  print("The given matrix in RREF is:")
  for row in matrix:
    print(row)
  return matrix

lin_sys = ["1x1 + 1x2 + 2x3 = 8", "-1x1 - 2x2 + 3x3 = 1", "3x1 - 7x2 + 4x3= 10"]

# Finding the augmented matrix
aug = []
for eqn in lin_sys:
  row = []
  for i in range(len(eqn)):
    if eqn[i] == 'x':
      if eqn[i - 2] == '-' or eqn[i - 3] == '-':
        row.append(-int(eqn[i - 1]))
      else:
        row.append(int(eqn[i - 1]))
    if eqn[i] == '=':
      row.append(int(eqn[i + 1:]))
  aug.append(row)
    
aug = rref(aug)
rank = len(aug)
zeros = [0] * len(aug[0])
solution = []
for row in aug:
  if row == zeros:
    rank -= 1
# Unique Solution
if rank == len(aug[0]) - 1:
  for i in range(len(aug) - 1, -1, -1):
    for j in range(len(aug[0]) - 1):
      if math.isclose(aug[i][j], 0.0):
        continue
      else:
        solution.insert(0, aug[i][len(aug[0]) - 1])
  print("Unique Solution:", solution)
# Infinite Solutions
elif rank < len(aug[0]) - 1:
  print("Infinite Solutions")
# No solution
else:
  print("No Solution")


