n = int(input())
i = 1
while i <= n:
    s = 1
    while s <= n-i:
        print(" ", end="")
        s += 1
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    p = i-1
    while p >= 1:
        print(p, end="")
        p -= 1
    print()
    i += 1
