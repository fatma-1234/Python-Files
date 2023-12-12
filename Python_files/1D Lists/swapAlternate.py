li = [int(x) for x in input().split()]
swapli = li.copy()
for i in range(1, len(swapli), 2):
    swapli[i], swapli[i-1] = swapli[i-1], swapli[i]
print(swapli)


# This program will show error with odd number of items
# because it will enter for loop as last element in the list
# and won't be able to do i+1 where as in upper program last element
# will change itself with i-1 because for loop is starting from 1

# li = [int(x) for x in input().split()]
# swapli = li.copy()
# for i in range(0, len(swapli), 2):
#     temp = swapli[i]
#     swapli[i] = swapli[i+1]
#     swapli[i+1] = temp
# print(swapli)
