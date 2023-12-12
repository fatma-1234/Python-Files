n = int(input())
i = 0
while i < n:
    j = 1
    while j <= (n-i):
        print(j, end="")
        j += 1
    print()
    i += 1
