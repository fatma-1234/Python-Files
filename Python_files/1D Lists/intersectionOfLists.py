fli = [int(x) for x in input().split()]
sli = [int(x) for x in input().split()]
m = len(fli)
n = len(sli)
for i in range(m):
    for j in range(n):
        if fli[i] == sli[j]:
            print(fli[i], end=" ")
