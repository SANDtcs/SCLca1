#Gauss Jacabi methid

lin_sys = ["2x + 5x2 = 21", "1x1 + 2x2 = 8"]
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


rows = len(aug)
columns = len(aug[0])
prev = [0] * (columns - 1)
solutions = [0] * (columns - 1)

for i in range(10):
  for j in range(rows):
    x = aug[j][columns - 1]
    for k in range(columns - 1):
      if k != j:
        x -= aug[j][k] * prev[k]
    solutions[j] = x / aug[j][j]

  print("Iteration", i + 1)
  print(solutions)
  for i in range(len(solutions)):
    prev[i] = solutions[i]
  print("\n")

for i in range(columns - 1):
    #print("x", i + 1, " = ", round(solutions[i]), sep = "")
    print("x", i + 1, " = ", solutions[i], sep = "")






#Gauss Seidal Method
lin_sys = ["3x + 1x2 = 11", "2x1 + 5x2 = 16"]
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

rows = len(aug)
columns = len(aug[0])
solutions = [0] * (columns - 1)
for i in range(10):
  for j in range(rows):
    x = aug[j][columns - 1]
    for k in range(columns - 1):
      if k != j:
        x -= aug[j][k] * solutions[k]
    solutions[j] = x / aug[j][j]
  print("Iteration", i + 1)
  print(solutions)
for i in range(columns - 1):
  print("x", i + 1, " = ", solutions[i], sep = "")
  
  
  
  
  #Gauss Seidal method 2
  print('\n\n*** GAUSS SEIDAL METHOD IMPLEMENTATION ***')
def seidal(a,b,x):
    n=len(a)   
    for i in range(0,n):
        d=b[i]
        for j in range(0,n):
            if(i!=j):
                d-=a[i][j]*x[j]
        x[i]=d/a[i][i]
            
    return x

x = [0, 0, 0]                        
a = [[2,3,-1],[3,2,1],[1,-5,3]]
b = [5,10,0]
for i in range(0,25):
    x=seidal(a,b,x)
    print(x)
    print()

new_list = [round(item) for item in x]
print("The answer is: ",new_list)
