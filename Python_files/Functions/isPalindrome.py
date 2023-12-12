def isPalin(num):
    rev = 0
    n = num
    while num > 0:
        l = num % 10
        rev = rev*10 + l
        num = num//10
    if rev == n:
        return True
    else:
        return False


n = int(input())
if isPalin(n):
    print("true")
else:
    print("false")
