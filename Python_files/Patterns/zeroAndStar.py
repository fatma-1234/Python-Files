n = int(input())
i = 1
while i <= n:
    j = 1
    while j <= (2*n)+1:
        if j == i or j == n+1 or j == ((2*n)+1)-i+1:
            print("*", end="")
        else:
            print("0", end="")
        j += 1
    print()
    i += 1

# another way using for loop
# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, (2*n)+2):
#         if j == i or j == n+1 or j == ((2*n)+1)-i+1:
#             print("*", end="")
#         else:
#             print("0", end="")
#         j += 1
#     print()
