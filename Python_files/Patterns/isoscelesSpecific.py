n = int(input())
i = 1
while i <= n:
    s = 1
    while s <= n-i:
        print(" ", end="")
        s += 1
    j = 1
    p = i
    while j <= i:
        print(p, end="")
        p += 1
        j += 1
    k = i-1
    p = 2*i-2
    while k >= 1:
        print(p, end="")
        p -= 1
        k -= 1
    print()
    i += 1


# another method
# n = int(input())
# for i in range(1, n+1):
#     for s in range(1, n-i+1):
#         print(" ", end="")
#     p = i
#     for j in range(1, i+1):
#         print(p, end="")
#         p += 1
#     p = 2*i-2
#     for k in range(i-1, 0, -1):
#         print(p, end="")
#         p -= 1
#     print()


# another method
# n = int(input())
# for i in range(1, n+1):
#     for s in range(1, n-i+1):
#         print(" ", end="")
#     for j in range(i, 2*i):
#         print(j, end="")
#     for k in range(2*i-2, i-1, -1):
#         print(k, end="")
#     print()
