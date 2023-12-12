li = [int(x) for x in input().split()]
n = len(li)
for i in range(0, n-1, 1):
    if li[i] > li[i+1]:
        print("Not sorted")
        break
else:
    print("Sorted")
