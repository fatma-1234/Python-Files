n = int(input())
num1 = n
num2 = n
digits = 0
while num1 > 0:
    digits += 1
    num1 = num1//10
arm = 0
while num2 > 0:
    l = num2 % 10
    arm += l**digits
    num2 = num2//10
if arm == n:
    print("true")
else:
    print("false")
