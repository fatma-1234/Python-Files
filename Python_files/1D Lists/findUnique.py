li = [int(x) for x in input().split()]
for i in range(len(li)):
    for j in range(len(li)):
        if i != j and li[i] == li[j]:
            break
    else:
        print(li[i])


# li = [int(x) for x in input().split()]
# for i in range(len(li)):
#     flag = False
#     for j in range(len(li)):
#         if i != j and li[i] == li[j]:
#             flag = True
#             break
#     if not (flag):
#         print(li[i])
