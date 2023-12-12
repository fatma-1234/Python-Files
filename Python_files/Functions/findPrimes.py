def is_prime(a):
    for i in range(2, a):
        if (a % i == 0):
            break
    else:
        return True
    return False


def find_prime(b):
    for b in range(2, b+1):
        if is_prime(b):
            print(b)


n = int(input("Enter a number: "))
find_prime(n)


# n = int(input())
# for k in range(2, n+1):
#     for i in range(2, k):
#         if (k % i == 0):
#             break
#     else:
#         print(k)
