def checkMember(n):
    a = 0
    b = 1
    i = 1
    while i <= n+1:
        c = a+b
        a = b
        b = c
        if a == n:
            ans = True
            return ans
        i += 1
    else:
        ans = False
        return ans


n = int(input())
if (checkMember(n)):
    print("true")
else:
    print("false")
