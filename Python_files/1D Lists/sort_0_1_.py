li = [int(x) for x in input().split()]
nextZero = 0
for i in range(len(li)):
    if li[i] == 0:
        li[nextZero], li[i] = li[i], li[nextZero]
        nextZero += 1
print(li)


# li = [int(x) for x in input().split()]
# zeros = [x for x in li if x == 0]
# ones = [x for x in li if x == 1]
# sorted_li = zeros + ones
# print(sorted_li)
