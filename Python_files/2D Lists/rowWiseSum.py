rows, cols = map(int, input().split())
mat = [[int(x) for x in input().split()] for i in range(rows)]

for i in range(rows):
    rowSum = 0
    for j in range(cols):
        rowSum += mat[i][j]
    print(rowSum)
