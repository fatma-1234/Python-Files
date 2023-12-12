n = int(input())
x = n
rev = 0

while n > 0:
    last = n % 10
    rev = rev*10 + last
    n = n//10

if rev == x:
    print("true")
else:
    print("false")
