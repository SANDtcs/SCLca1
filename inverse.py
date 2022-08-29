arr = np.zeros((3, 3, 3), dtype = 'int')

arr[0] = [[2, 3, 1],
          [0, -1, 2],
          [0, 0, 3]]

arr[1] = [[3, 0, 0],
          [1, -1, 0],
          [0, 2, 8]]

arr[2] = [[1, 2, 0],
          [0, -7, 1],
          [0, 0, 0]]

for i in range(len(arr)):
  n = len(arr[i])
  eigenVector = np.array([[1]] * n)
  if np.linalg.det(arr[i]) != 0:
    inv = np.linalg.inv(arr[i])
  else:
    continue
  for j in range(20):
    eigenVector = np.matmul(inv, eigenVector)
    eigenVector = np.round(eigenVector / max(eigenVector), 2)
  eigenValue = round(sum(np.matmul(inv, eigenVector) * eigenVector)[0] / (sum(eigenVector * eigenVector)[0]), 2)
  print(f'{i + 1}. Smallest Eigenvalue = {eigenValue}')
  print(f'Smallest Eigenvector = \n{eigenVector}', end = '\n\n')
