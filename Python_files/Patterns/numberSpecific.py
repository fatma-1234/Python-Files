n = int(input("Enter the value of n: "))
i = 1

while i <= n:
    j = 1

    # Print increasing numbers
    while j <= i:
        print(j, end='')
        j += 1

    # Print spaces
    spaces = 2 * (n - i)
    while spaces > 0:
        print(' ', end='')
        spaces -= 1

    # Print decreasing numbers
    j = i
    while j > 0:
        print(j, end='')
        j -= 1

    print()  # Move to the next line for the next row
    i += 1
