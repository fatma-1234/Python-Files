while True:
    n = int(input())
    if n % 2 == 0:
        print("Please enter odd number")
    else:
        a = (n+1)/2
        b = a-1
        i = 1
        while i <= a:
            s = 1
            while s < i:
                print(" ", end="")
                s += 1
            j = 1
            while j <= i:
                print("* ", end="")
                j += 1
            print()
            i += 1
        while b >= 1:
            s = b
            while s > 1:
                print(" ", end="")
                s -= 1
            j = b
            while j >= 1:
                print("* ", end="")
                j -= 1
            print()
            b -= 1
        break
