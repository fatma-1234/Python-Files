li = [int(sum) for sum in input().split()]
sum = int(input())
count = 0
for i in range(len(li)):
    for j in range(i+1, len(li)):
        for k in range(j+1, len(li)):
            if li[i]+li[j]+li[k] == sum:
                count += 1
print(count)


# li = [int(sum) for sum in input().split()]
# sum = int(input())
# count = 0
# for i in range(len(li)):
#     for j in range(i, len(li)):
#         for k in range(j, len(li)):
#             if i != j != k and li[i]+li[j]+li[k] == sum:
#                 count += 1
# print(count)
