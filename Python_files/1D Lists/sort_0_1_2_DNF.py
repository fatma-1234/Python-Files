li = [int(x) for x in input().split()]
low, high = 0, len(li) - 1
i = 0
while i <= high:
    if li[i] == 0:
        li[low], li[i] = li[i], li[low]
        low += 1
        i += 1
    elif li[i] == 1:
        i += 1
    else:
        li[i], li[high] = li[high], li[i]
        high -= 1
print(li)
