rows, cols = map(int, input().split())
mat = [[int(x) for x in input().split()] for i in range(rows)]

larMatSum = float('-inf')
larMat = 0

for i in range(rows):
    matSum = 0
    for j in range(cols):
        matSum += mat[i][j]
    if matSum > larMatSum:
        larMatSum = matSum
        larMat = i+1
        flag = True

for j in range(cols):
    matSum = 0
    for i in range(rows):
        matSum += mat[i][j]
    if matSum > larMatSum:
        larMatSum = matSum
        larMat = j+1
        flag = False

if flag:
    print("Largest Row is", larMat, "and the sum is", larMatSum)
else:
    print("Largest Column is", larMat, "and the sum is", larMatSum)
