n = int(input())
a = 0
b = 1
for i in range(1, n):
    c = a+b
    a = b
    b = c
print(a)


# n = int(input())
# a = 0
# b = 1
# i = 1
# while i < n:
#     c = a+b
#     a = b
#     b = c
#     i += 1
# print(a)
