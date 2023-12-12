li = [int(x) for x in input().split()]
n = len(li)

for i in range(1, n):
    j = i - 1
    key = li[i]
    while j >= 0 and key < li[j]:
        li[j + 1] = li[j]
        j -= 1
    li[j + 1] = key
print(li)
