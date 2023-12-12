num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
min = num1 if num1 <= num2 else num2
hcf = 1
for i in range(1, min+1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("The highest common factor is", hcf)


# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# if num1 <= num2:
#     min = num1
# else:
#     min = num2
# hcf = 1
# for i in range(1, min+1):
#     if num1 % i == 0 and num2 % i == 0:
#         hcf = i
# print("The highest common factor is", hcf)
