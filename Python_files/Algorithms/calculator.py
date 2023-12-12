# If the input is 1, then 2 integers are taken from the user and their sum is printed.
# If the input is 2, then 2 integers are taken from the user and their difference(1st number - 2nd number) is printed.
# If the input is 3, then 2 integers are taken from the user and their product is printed.
# If the input is 4, then 2 integers are taken from the user and the quotient obtained (on dividing 1st number by 2nd number)' printed.
# If the input is 5, then 2 integers are taken from the user and their remainder(1st number mod 2nd number) is printed.
# If the input is 6, then the program exits.
# For any other input, then print "Invalid Operation.

while True:
    choice = int(input())
    if (choice <= 5 and choice >= 1):
        a = int(input())
        b = int(input())
        if choice == 1:
            print(a+b)
        elif choice == 2:
            print(a-b)
        elif choice == 3:
            print(a*b)
        elif choice == 4:
            print(int(a/b))
        else:
            print(a % b)
    elif choice != 6:
        print("Invalid Operation")
    else:
        break
