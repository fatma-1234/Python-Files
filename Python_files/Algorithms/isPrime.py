n = int(input("Enter a number to check whether it is prime or not: "))
for i in range(2, n):
    if n % i == 0:
        print("This is not a prime number")
        break
else:
    print("Yes this is a prime number")


# another way for the same program using for loop
# n = int(input())
# flag = False
# for i in range(2, n):
#     if n % i == 0:
#         flag = True
# if flag:
#     print("not prime")
# else:
#     print("prime")


# n = int(input())
# i = 2
# flag = False
# while i < n:
#     if (n % i == 0):  # consider it's a switch
#         flag = True   # this is a switch
#     i += 1
# if flag:
#     print("not prime")
# else:
#     print("prime")
