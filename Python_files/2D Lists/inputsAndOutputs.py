# rows = int(input())
# cols = int(input())
# mat = []
# for i in range(rows):
#     temp = []
#     for j in range(cols):
#         temp.append(int(input()))
#     mat.append(temp)


# inputs = [int(x) for x in input().split()]
# rows = inputs[0]
# cols = inputs[1]
# mat = [[inputs[2+cols*i+j] for j in range(cols)] for i in range(rows)]


rows, cols = map(int, input().split())
mat = [[int(x) for x in input().split()] for i in range(rows)]


for row in mat:
    for ele in row:
        print(ele, end=" ")
    print()


# for i in range(rows):
#     for j in range(cols):
#         print(mat[i][j], end=" ")
#     print()


# for row in mat:
#     print(" ".join([str(ele) for ele in row]))
