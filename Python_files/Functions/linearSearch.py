def linsearch(li, ele):
    for i in range(len(li)):
        if ele == li[i]:
            return i+1
    return "Not Found"


li = [int(x) for x in input().split()]
num = int(input())
p = linsearch(li, num)
print(p)
