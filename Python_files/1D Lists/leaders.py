li = [int(x) for x in input().split()]

leaders = [li[len(li)-1]]

for i in range(len(li)-2, -1, -1):
    if li[i] >= leaders[len(leaders)-1]:
        leaders.append(li[i])

for i in range(len(leaders)-1, -1, -1):
    print(leaders[i], end=" ")
