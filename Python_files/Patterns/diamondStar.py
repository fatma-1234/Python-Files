while True:
    n = int(input())
    if n % 2 == 0:
        print("Please enter an odd number")
    else:
        a = (n+1)//2
        b = a-1

        for i in range(1, a+1):
            for j in range(1, a-i+1):
                print(" ", end="")
            for k in range(1, (2*i)):
                print("*", end="")
            print()

        for i in range(b, 0, -1):
            for j in range(1, b-i+2):
                print(" ", end="")
            for k in range(1, (2*i)):
                print("*", end="")
            print()
        break


# while True:
#     n = int(input())
#     if n % 2 == 0:
#         print("Please enter odd number")
#     else:
#         a = (n+1)/2
#         b = a-1
#         i = 1
#         while i <= a:
#             j = 1
#             while j <= a-i:
#                 print(" ", end="")
#                 j += 1
#             k = 1
#             while k <= (2*i)-1:
#                 print("*", end="")
#                 k += 1
#             print()
#             i += 1
#         i = b
#         while i >= 1:
#             j = 1
#             while j <= b-i+1:
#                 print(" ", end="")
#                 j += 1
#             k = 1
#             while k <= (2*i)-1:
#                 print("*", end="")
#                 k += 1
#             print()
#             i -= 1
#         break
