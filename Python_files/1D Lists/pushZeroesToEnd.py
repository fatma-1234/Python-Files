li = [int(x) for x in input().split()]
f = 0
l = len(li) - 1
new = [0] * len(li)
for i in range(len(li)):
    if li[i] != 0:
        new[f] = li[i]
        f += 1
    else:
        new[l] = li[i]
        l -= 1
print(new)

# li = [int(x) for x in input().split()]
# new = []
# i = 0
# for ele in li:
#     if ele != 0:
#         new.insert(i, ele)
#         i += 1
#     else:
#         new.append(0)
# print(new)
