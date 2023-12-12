
n = int(input())
esum = 0
osum = 0
while n > 0:
    l = n % 10
    if l % 2 == 0:
        esum = esum+l
    else:
        osum = osum+l
    n = n//10
print(esum, osum)
