n = int(input())
a = 0
b = 1
i = 1
flag = False
while i <= n+1:
    c = a+b
    a = b
    b = c
    if a == n:
        flag = True
        break
    i += 1

if flag:
    print("yes")
else:
    print("not")
