def reverse(li):
    return li[::-1]


li = [int(x) for x in input().split()]
revli = reverse(li)
print(revli)


# def reverse(li):
#     length = len(li)
#     for i in range(length//2):
#         temp = li[i]
#         li[i] = li[length-i-1]            #li[i] = li[-i-1]   can also be done
#         li[length-i-1] = temp             #li[-i-1] = temp    it's negative indexing
# li = [int(x) for x in input().split()]
# reverse(li)
# print(li)
