rows, cols = map(int, input().split())
mat = [[int(x) for x in input().split()] for i in range(rows)]


for j in range(cols):
    for i in range(rows):
        if j % 2 == 0:
            print(mat[i][j], end=" ")
        else:
            print(mat[rows-i-1][j], end=" ")
