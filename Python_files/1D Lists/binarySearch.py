li = [int(x) for x in input().split()]
num = int(input())
low = 0
high = len(li) - 1

while low <= high:
    medium = (low + high) // 2
    if li[medium] == num:
        print(medium + 1)
        break
    elif li[medium] < num:
        low = medium + 1
    else:
        high = medium - 1
else:
    print("Number not found in the list")


# li = [int(x) for x in input().split()]
# num = int(input())
# low = 0
# high = len(li) - 1
# flag = False
# while low <= high:
#     medium = (low + high) // 2
#     if li[medium] == num:
#         flag = True
#         print(medium + 1)
#         break
#     elif li[medium] < num:
#         low = medium + 1
#     else:
#         high = medium - 1
# if not flag:
#     print("Number not found in the list")
