def isArm(num):
    num1 = num
    num2 = num
    digits = 0
    while num1 > 0:
        digits += 1
        num1 = num1//10
    arm = 0
    while num2 > 0:
        l = num2 % 10
        arm += l**digits
        num2 = num2//10
    if arm == num:
        return True
    else:
        return False


n = int(input())
ans = isArm(n)
if ans:
    print("true")
else:
    print("false")
