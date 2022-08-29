from cmath import isclose
def nonzero(row):
    for i in range(len(row)):
        if row[i]!=0:
            return i

def rref(matrix):
    rows = len(matrix)
    cols = len(matrix[1])
    matrix.sort(key = nonzero)

    for i in range(rows):
        for j in range(cols):
            if not isclose(matrix[i][j],0.0):
                matrix[i] = [x/matrix[i][j] for x in matrix[i]]
                break

        for k in range(rows):
            if k == i:
                continue
            else:
                row = [matrix[k][j]*x for x in matrix[i]]
                matrix[k] = [x-y for x,y in zip(matrix[k],row)]
    for row in matrix:
        print(row)
    return matrix

def soln(aug):
    matrix = rref(aug)
    zeroes = [0]*len(aug[0])
    rank = len(aug)
    solution = []
    for row in aug:
        if row == zeroes:
            rank = rank -1
    if rank == len(aug[0]) - 1:
        for i in range(len(aug)-1,-1,-1):
            for j in range(len(aug[0])-1):
                if isclose(aug[i][j],0.0):
                    continue
                else:
                    solution.insert(0,aug[i][len(aug[0])-1])
        print("unique soln",solution)
    elif rank < len(aug) - 1:
        print("infinte soln")
    else:
        print("no soln")



aug = [[1,1,2,8],
        [-1,-2,3,1],
        [3,-7,4,10]]
soln(aug)