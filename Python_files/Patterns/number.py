n = int(input())
i = 1
while i <= n:
    j = 1
    p = i
    while j <= i:
        print(p, end="")
        j += 1
        p += 1
    print()
    i += 1


# same program using for loop
# n = int(input())
# for i in range(1, n+1, 1):
#     p = i
#     for j in range(1, i+1, 1):
#         print(p, end="")
#         p += 1
#     print()
