num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
max = num1 if num1 >= num2 else num2
lcm = max
while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += max
print("The lowest common multiple is", lcm)


# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# if num1 >= num2:
#     max = num1
# else:
#     max = num2
# lcm = max
# while True:
#     if lcm % num1 == 0 and lcm % num2 == 0:
#         break
#     lcm += max
# print("The lowest common multiple is", lcm)
