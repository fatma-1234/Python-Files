N = int(input("Enter the total number of rows : "))
n = N
row = N
while n > 0:
    j = 1
    while j <= n:
        print(j, end="")
        j = j+1
    print((2*(N - row))*"*", end="")
    row -= 1
    i = n
    while i > 0:
        print(i, end="")
        i = i-1
    print()
    n = n-1
