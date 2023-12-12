li = [int(x) for x in input().split()]

highest, second_highest = (li[1], li[0]) if li[0] <= li[1] else (li[0], li[1])

for num in li:
    if num > highest:
        second_highest = highest
        highest = num
    elif num > second_highest and num != highest:
        second_highest = num

print(second_highest)
