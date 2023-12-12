n = int(input())
for i in range(1, n+1):
    for s in range(1, i):
        print(" ", end="")
    for p in range(i, n+1):
        print(p, end="")
    print()
for i in range(n-1, 0, -1):
    for s in range(i-1, 0, -1):
        print(" ", end="")
    for p in range(i, n+1):
        print(p, end="")
    print()
