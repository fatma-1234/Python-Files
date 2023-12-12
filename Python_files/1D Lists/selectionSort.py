li = [int(x) for x in input().split()]
n = len(li)
for i in range(n):
    min = i
    for j in range(i + 1, n):
        if li[j] < li[min]:
            min = j
    li[i], li[min] = li[min], li[i]
print(li)
