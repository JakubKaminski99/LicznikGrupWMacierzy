def count(matrix):
    groups = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                groups += 1
                flow(matrix, i, j)
    return groups

def flow(matrix, row, column):
    if  row < 0 or row >= len(matrix) or column < 0 or column >= len(matrix[0]) or matrix[row][column] == 1:
        return
    matrix[row][column] = 1
    drow = [-1,0,1,0]
    dcolumn = [0,1,0,-1]
    for k in range(len(drow)):
        flow(matrix, row + drow[k], column + dcolumn[k])
    return

mat = [[0,0,1,1],[1,1,0,0],[1,0,1,1],[1,0,1,1],[0,0,0,0]]
print(count(mat))

#0000
#1111
#0000
#1111