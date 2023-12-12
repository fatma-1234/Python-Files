def isSorted(li):
    n = len(li)
    for i in range(0, n-1, 1):
        if li[i] > li[i+1]:
            return False
    return True


li = [int(x) for x in input().split()]
if isSorted(li):
    print("Sorted")
else:
    print("Not sorted")
