n = int(input())
i = 1
while i <= n:
    s = 1
    while s <= n-i:
        print(" ", end="")
        s += 1
    p = i
    while p >= 1:
        print(p, end="")
        p -= 1
    p = 2
    while p <= i:
        print(p, end="")
        p += 1
    print()
    i += 1
