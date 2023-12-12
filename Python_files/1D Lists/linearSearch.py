li = [int(x) for x in input().split()]
num = int(input())
for i in range(len(li)):
    if num == li[i]:
        print(i+1)
        break
else:
    print("Not Found")


# li = [int(x) for x in input().split()]
# num = int(input())
# flag = False
# for i in range(len(li)):
#     if num == li[i]:
#         print(i+1)
#         flag = True
#         break
# if not (flag):
#     print("Not Found")
