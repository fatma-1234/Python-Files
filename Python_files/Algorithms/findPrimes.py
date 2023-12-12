n = int(input())
for k in range(2, n+1):
    for i in range(2, k):
        if (k % i == 0):
            break
    else:
        print(k)


# n = int(input())
# for k in range(2, n+1):
#     flag = False
#     for i in range(2, k):
#         if (k % i == 0):
#             flag = True
#     if not (flag):
#         print(k)


# n = int(input())
# k = 2
# while k <= n:
#     i = 2
#     flag = False
#     while i < k:
#         if (k % i == 0):
#             flag = True
#         i += 1
#     if not (flag):
#         print(k)
#     k += 1
