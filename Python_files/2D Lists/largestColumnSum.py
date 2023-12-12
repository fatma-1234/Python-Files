rows, cols = map(int, input().split())
mat = [[int(x) for x in input().split()] for i in range(rows)]

larColSum = float('-inf')
larCol = 0

for j in range(cols):
    colSum = 0
    for i in range(rows):
        colSum += mat[i][j]
    if colSum > larColSum:
        larColSum = colSum
        larCol = j+1

print(larCol, larColSum)
