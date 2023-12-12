rows, cols = map(int, input().split())
mat = [[int(x) for x in input().split()] for i in range(rows)]

top, right, bottom, left = 0, cols - 1, rows - 1, 0

while left <= right and top <= bottom:

    for j in range(left, right + 1):
        print(mat[top][j], end=" ")
    top += 1

    for i in range(top, bottom + 1):
        print(mat[i][right], end=" ")
    right -= 1

    # if top is still less than bottom because we have incremented top
    if top <= bottom:
        for j in range(right, left - 1, -1):
            print(mat[bottom][j], end=" ")
        bottom -= 1

    # if left is still less than right because we have decremented right
    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(mat[i][left], end=" ")
        left += 1
