def is_prime(a):
    for i in range(2, a):
        if n % i == 0:
            print("This is not a prime number")
            break
    else:
        print("Yes this is a prime number")


n = int(input("Enter a number to check whether it is prime or not: "))
is_prime(n)


# n = int(input("Enter a number to check whether it is prime or not: "))
# for i in range(2, n):
#     if n % i == 0:
#         print("This is not a prime number")
#         break
# else:
#     print("Yes this is a prime number")
