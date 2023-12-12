li = [int(sum) for sum in input().split()]
sum = int(input())
count = 0
for i in range(len(li)):
    for j in range(i+1, len(li)):
        if li[i]+li[j] == sum:
            count = count + 1
print(count)


# li = [int(sum) for sum in input().split()]
# sum = int(input())
# count = 0
# for i in range(len(li)):
#     for j in range(i, len(li)):
#         if i != j and li[i]+li[j] == sum:
#             count += 1
# print(count)
