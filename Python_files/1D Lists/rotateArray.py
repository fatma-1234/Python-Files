li = [int(x) for x in input().split()]
n = len(li)
d = int(input())
d = d % n
temp = [0] * d
for i in range(d):
    temp[i] = li[i]
for i in range(n - d):
    li[i] = li[i + d]
for i in range(d):
    li[n - d + i] = temp[i]
print(li)
