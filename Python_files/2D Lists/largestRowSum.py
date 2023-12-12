rows, cols = map(int, input().split())
mat = [[int(x) for x in input().split()] for i in range(rows)]

larRowSum = float('-inf')
larRow = 0

for i in range(rows):
    rowSum = 0
    for j in range(cols):
        rowSum += mat[i][j]
    if rowSum > larRowSum:
        larRowSum = rowSum
        larRow = i+1

print(larRow, larRowSum)
