rows, cols = map(int, input().split())
mat = [[int(x) for x in input().split()] for i in range(rows)]

for i in range(rows):
    for k in range(rows - i):
        for j in range(len(mat[i])):
            print(mat[i][j], end=" ")
        print()
